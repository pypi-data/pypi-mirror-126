import abc
import json
from operator import itemgetter

from django.contrib.postgres.aggregates import StringAgg
from django.db import transaction
from django.db.models import (
    Value,
    F,
    BooleanField,
    Case,
    When,
    Q,
    Func,
    CharField,
    Count,
)
from django.db.models.functions import Cast
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.views.generic import DetailView, TemplateView

from report_designer.consts import Functions
from report_designer.core.utils import order_by_list
from report_designer.core.views import (
    TitleMixin,
    AjaxContentListView,
    ParentMixin,
    ObjectActionAjaxView,
    DynamicContentTableBaseView,
    CreateAjaxView,
    ActionGroupMixin,
    UpdateAjaxView,
    BreadcrumbsListMixin,
    BackUrlDetailMixin,
    BreadcrumbsDetailMixin,
    Select2BaseListView,
    AjaxResponseMixin, CustomDeleteView,
)
from report_designer.models import (
    Report,
    DBTable,
    TableField,
    ReportField,
    ReportFieldRelation,
    ReportTableRelation,
    ReportTable,
)
from report_designer.reports.actions import (
    ReportListActionGroup,
    ReportDropdownActionGroup,
    ReportAddFieldActionGroup,
    ReportTableRelationActionGroup,
    ReportAddVirtualFieldActionGroup,
)
from report_designer.reports.filters import (
    ReportFilterSet,
    ReportFieldsFilterSet,
    ReportTableRelationFilterSet,
)
from report_designer.reports.forms import (
    ReportCreateForm,
    ReportCreateByReportForm,
    ReportUpdateForm,
    ReportTableRelationCreateUpdateForm,
    ReportTableRelationConditionsFormsetManager,
    ReportFieldUpdateForm,
    ReportVirtualFieldCreateUpdateForm,
)
from report_designer.reports.report_handler import ReportCloneHandler
from report_designer.reports.tables import (
    ReportsTable,
    ReportFieldsTable,
    ReportTableRelationTable,
)


# endregion Базовые миксины


class ReportBreadcrumbsListMixin(BreadcrumbsListMixin):
    """
    Хлебные крошки отчетов
    """

    title_breadcrumb = 'Список отчетов'


class ReportBreadcrumbsDetailBaseMixin(BreadcrumbsDetailMixin, ReportBreadcrumbsListMixin):
    """
    Хлебные крошки отчета
    """

    pass


class ReportsDynamicContentTableBaseView(ParentMixin, DynamicContentTableBaseView):
    """
    Базовое представление для динамических список на странице отчета
    """

    parent_model = Report
    is_paginate = False

    def get_content_url_kwargs(self):
        content_url_kwargs = super().get_content_url_kwargs()
        content_url_kwargs.update(pk=self.parent.pk)
        return content_url_kwargs


# endregion Базовые миксины


# region Список отчетов


class ReportListView(ReportBreadcrumbsListMixin, DynamicContentTableBaseView):
    """
    Представление: Список отчетов
    """

    model = Report
    filterset_class = ReportFilterSet
    table_class = ReportsTable
    title = 'Отчеты'
    ajax_content_name = 'reports'
    action_group_classes = (ReportListActionGroup,)


# endregion Список отчетов


# region Создание / редактирование отчета


class ReportCreateUpdateMixin:
    """
    Миксин создания / редактирования отчета
    """

    model = Report

    def get_success_redirect_url(self):
        return self.object.get_detail_url()


class BaseReportCreateView(ReportCreateUpdateMixin, CreateAjaxView):
    """
    Базовое представление: Создание отчета
    """

    title = 'Создание отчета'
    form_class = ReportCreateForm

    def set_object_additional_values(self, obj):
        super().set_object_additional_values(obj)
        obj.author = self.request.user


class ReportCreateView(BaseReportCreateView):
    """
    Представление: Создание отчета
    """

    form_class = ReportCreateForm

    def after_save(self, **kwargs):
        super().after_save(**kwargs)
        self.object.report_tables.create(report=self.object, db_table=self.object.root, is_root=True)


class ReportCreateByReportView(BaseReportCreateView):
    """
    Представление: Создание отчета на основании другого отчета
    """

    form_class = ReportCreateByReportForm

    def after_save(self, **kwargs):
        super().after_save(**kwargs)
        form = kwargs.get('form')
        ReportCloneHandler(form.cleaned_data.get('report'), self.object).run()


class ReportUpdateView(ReportCreateUpdateMixin, UpdateAjaxView):
    """
    Представление: Редактирование отчета
    """

    title = 'Редактирование отчета'
    form_class = ReportUpdateForm


# endregion Создание / редактирование отчета


# region Просмотр отчета


class ReportDetailView(
    BackUrlDetailMixin,
    ReportBreadcrumbsDetailBaseMixin,
    ActionGroupMixin,
    TitleMixin,
    DetailView,
):
    """
    Представление: Просмотр отчета
    """

    model = Report
    template_name = 'report_designer/reports/detail.html'
    context_object_name = 'report'
    action_group_classes = (
        ReportDropdownActionGroup,
        ReportAddFieldActionGroup,
        ReportTableRelationActionGroup,
        ReportAddVirtualFieldActionGroup,
    )

    def get_title(self):
        return f'Отчет "{self.object.name}"'


# endregion Просмотр отчета


# region Редактирование списка таблиц в отчете


class BaseTreeListView(AjaxContentListView):
    """
    Базовое представления для вывода дерева
    """

    is_paginate = False
    is_only_ajax = True
    is_subtree = False
    template_name = 'report_designer/reports/blocks/tables_tree_branch.html'
    context_object_name = 'tree_branches'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(
            {
                'is_subtree': self.is_subtree,
            }
        )
        return context_data


class ExpressionsMixin:
    """
    Миксин для полей для составления выражений
    """

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({'is_expression': self.is_expression})
        return context_data

    @property
    def is_expression(self):
        """
        Неперносимыое (кликабельное) поле
        """
        return 'is_expression' in self.request.GET


class DBTablesBaseTreeListView(ParentMixin, BaseTreeListView):
    """
    Базовое представление: Список таблиц БД / в отчете
    """

    queryset = DBTable.objects.available()
    context_object_name = 'tree_branches'
    parent_model = Report
    kwargs_parent_fk = 'report_pk'
    parent_context_name = 'report'
    is_processed = False

    def get_queryset(self):
        # Аннотация параметров для списка таблиц
        # 1). PK для URL загрузки полей
        # 2). Title из alias
        # 3). Существование связи для URL загрузки полей
        return (
            super()
            .get_queryset()
            .annotate(
                related_table_pk=F('pk'),
                title=F('alias'),
                is_relation=Value(True, output_field=BooleanField()),
            )
        )

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({'is_processed': self.is_processed})
        return context_data


class ActionTablesMixin:
    """
    Миксин добавления URL действия с таблицами
    """

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({'action_url': self.get_action_tables_url()})
        return context_data

    @abc.abstractmethod
    def get_action_tables_url(self):
        """
        URL для действия с таблицами
        """
        raise NotImplementedError


class DBTablesTreeListView(ActionTablesMixin, DBTablesBaseTreeListView):
    """
    Представление: Список таблиц БД
    """

    def get_action_tables_url(self):
        return reverse_lazy('report_designer:reports:add-table', kwargs={'pk': self.parent.pk})


class ReportDBTablesTreeListView(ActionTablesMixin, DBTablesBaseTreeListView):
    """
    Представление: Список таблиц в отчете
    """

    is_processed = True

    def get_queryset(self):
        # Доступны таблицы, добавленные в отчет
        return super().get_queryset().for_report(self.parent)

    def get_action_tables_url(self):
        return reverse_lazy('report_designer:reports:remove-table', kwargs={'pk': self.parent.pk})


class TableFieldsListView(ExpressionsMixin, ParentMixin, BaseTreeListView):
    """
    Представление: Список таблиц БД / в отчете
    """

    queryset = TableField.objects.is_visible()
    parent_model = DBTable
    parent_field = 'db_table'
    is_subtree = True

    def get_queryset(self):
        queryset = super().get_queryset()

        # Цепочка связи
        chain = self.request.GET.get('chain', '')
        if self.is_processed:
            # Аннотация хеша цепочки связей полей отчета
            chain_kwargs = Func(
                StringAgg(
                    Cast(
                        Case(When(report_fields__report__pk=self.report.pk, then=F('report_fields__relations'))),
                        output_field=CharField(),
                    ),
                    delimiter=',',
                ),
                function='md5',
            )
            # Поля таблиц БД в полях очтета
            fields_in_report_fields = self.report.report_fields.values_list('field', flat=True)

            # Условие принадлежности поля к отчету
            condition = (
                chain
                and When(chain=Value(chain), then=Value(True))
                or When(pk__in=fields_in_report_fields, chain__isnull=True, then=Value(True))
            )
            is_exists_in_report_kwargs = Case(condition, default=Value(False), output_field=BooleanField())
            queryset = queryset.annotate(chain=chain_kwargs).annotate(is_exists_in_report=is_exists_in_report_kwargs)

        # Аннотации для составления выражений
        if self.is_expression:
            # Аннотация параметров поля
            field = Functions.Keywords.FIELD
            queryset = queryset.annotate(
                expression_field_name=Value(field, output_field=CharField()),
                expression_field_display_name=Value(Functions.Keywords.DISPLAY_NAMES.get(field), output_field=CharField()),
                expression_field_value=F('db_field'),
                expression_field_is_editable=Value(False, output_field=BooleanField()),
            )
        return queryset.with_related_tables(self.parent).with_title().order_by('is_relation', 'related_table_pk', 'pk')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(
            {
                'report': self.report,
                'is_processed': self.is_processed,
            }
        )
        return context_data

    @property
    def is_processed(self):
        """
        Переносимые поля
        """
        return 'is_processed' in self.request.GET

    @cached_property
    def report(self):
        """
        Отчет
        """
        return get_object_or_404(Report, pk=self.kwargs.get('report_pk'))


class ReportDBTableChangeBaseView(ObjectActionAjaxView):
    """
    Базовое представление: Добавление / удаление таблицы в отчете
    """

    model = Report
    join_errors = True
    dependents = (('ajax_contents', 'report_tables'),)

    @cached_property
    def table(self):
        """
        Добавляемая таблица
        """
        return get_object_or_404(DBTable.objects.available(), pk=self.request.POST.get('table'))


class ReportDBTableAddView(ReportDBTableChangeBaseView):
    """
    Представление: Добавление таблицы в отчет
    """

    title = 'Добавление таблицы в отчет'

    def valid_action(self):
        is_valid = super().valid_action()
        if self.object.report_tables.filter(db_table=self.table).exists():
            self.add_error(f'Таблица "{self.table.alias}" уже добавлена в отчет')
            is_valid = False
        return is_valid

    def action(self):
        super().action()
        self.object.report_tables.create(db_table=self.table, order=self.object.table_next_order)


class ReportDBTableRemoveView(ReportDBTableChangeBaseView):
    """
    Представление: Удаление таблицы из отчета
    """

    title = 'Удаление таблицы из отчета'

    def valid_action(self):
        is_valid = super().valid_action()
        if not self.object.report_tables.filter(db_table=self.table).exists():
            self.add_error(f'Таблица "{self.table.alias}" не существует в отчете')
            is_valid = False
        if self.table == self.object.root:
            self.add_error(f'Таблица "{self.table.alias}" является основной таблицей отчета')
            is_valid = False
        return is_valid

    def action(self):
        super().action()
        # Удаление таблицы из отчета
        report_table = self.object.report_tables.filter(db_table=self.table)
        order = report_table.first().order
        report_table.delete()

        # Изменение порядка таблиц
        self.object.report_tables.filter(order__gt=order).update(order=F('order') - 1)


# endregion Редактирование списка таблиц в отчете


# region Список связей таблиц отчета


class ReportTableRelationsListView(ReportsDynamicContentTableBaseView):
    """
    Представление: Список связей таблиц отчета
    """

    queryset = ReportTableRelation.objects.all()
    parent_field = 'report_table__report'
    table_class = ReportTableRelationTable
    filterset_class = ReportTableRelationFilterSet
    ajax_content_name = 'report_table_relations'

    def get_filterset_kwargs(self, filterset_class):
        filterset_kwargs = super().get_filterset_kwargs(filterset_class)
        filterset_kwargs.update({'report': self.parent})
        return filterset_kwargs


class ReportTableRelationCreateUpdateMixin(ParentMixin):
    """
    Миксин: Создание / редактирование связи таблицы отчета
    """

    template_name = 'report_designer/reports/create_table_relation.html'
    parent_model = Report
    kwargs_parent_fk = 'report_pk'
    model = ReportTableRelation
    title = 'Создание связи таблицы отчета'
    form_class = ReportTableRelationCreateUpdateForm
    formset_managers = (ReportTableRelationConditionsFormsetManager,)
    dependents = (('dynamic_contents', 'report_table_relations'),)

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs.update(report=self.parent)
        return form_kwargs

    def get_formset_managers_kwargs(self, **kwargs):
        formset_managers_kwargs = super().get_formset_managers_kwargs(**kwargs)
        formset_managers_kwargs.update(kwargs_relation_conditions={'report': self.parent})
        return formset_managers_kwargs


class ReportTableRelationCreateView(ReportTableRelationCreateUpdateMixin, CreateAjaxView):
    """
    Представление: Создание связи таблицы отчета
    """

    title = 'Создание связи таблицы отчета'

    def after_save(self, **kwargs):
        super().after_save(**kwargs)
        # Если связь для таблицы первая
        if self.object.report_table.relations.count() == 1:
            # Обновление связей таблиц для полей, не имеющих этих связей
            report_fields = self.parent.report_fields.filter(
                report_table_relation__isnull=True,
                field__db_table=self.object.report_table.db_table,
            )
            report_fields.update(report_table_relation=self.object)


class ReportTableRelationUpdateView(ReportTableRelationCreateUpdateMixin, UpdateAjaxView):
    """
    Представление: Создание связи таблицы отчета
    """

    title = 'Редактирование связи таблицы отчета'


# endregion Список связей таблиц отчета


# region Список полей в отчете


class ReportFieldsListView(ReportsDynamicContentTableBaseView):
    """
    Представление: Список полей отчета
    """

    queryset = ReportField.objects.order_by('order')
    parent_field = 'report'
    table_class = ReportFieldsTable
    filterset_class = ReportFieldsFilterSet
    ajax_content_name = 'report_fields'


class ReportFieldsDeleteView(CustomDeleteView):
    """
    Представление: Удаление поля отчета
    """

    model = ReportField
    dependents = (('ajax_contents', 'report_fields'),)


class ReportFieldsAddView(ObjectActionAjaxView):
    """
    Представление: Добавление полей в отчет
    """

    model = Report
    dependents = (
        ('ajax_contents', 'report_tables'),
        ('dynamic_contents', 'report_fields'),
    )

    @transaction.atomic
    def action(self):
        # Создание полей очтета
        table_fields_ids = list(map(itemgetter(-1), self.fields_with_relations))

        # Список полей, отсортированных в полученном порядке
        fields = order_by_list(TableField.objects.filter(pk__in=table_fields_ids), 'pk', table_fields_ids)

        # Последний порядковый номер поля в отчете
        order = self.object.field_next_order

        # Связи полей и поля
        relations_report_fields, report_fields = [], []
        for index, field in enumerate(fields):
            # Добавление поля отчета
            report_field = ReportField(
                name=field.name,
                alias=field.alias,
                representation=field.representation,
                report=self.object,
                field=field,
                order=order + index,
            )
            report_fields.append(report_field)
        objs = ReportField.objects.bulk_create(report_fields)

        # Добавление связей поля
        for report_field, chain in zip(objs, self.fields_with_relations):
            for relation_order, table_field_id in enumerate(chain[:-1]):
                relations_report_fields.append(
                    ReportFieldRelation(order=relation_order, report_field=report_field, table_field_id=table_field_id)
                )
        ReportFieldRelation.objects.bulk_create(relations_report_fields)

    @cached_property
    def fields_with_relations(self):
        """
        Список цепочек полей
        """
        fields_chains = self.request.POST.get('fields_chains[]')
        if not fields_chains:
            return {}
        return json.loads(fields_chains)


class ReportFieldChangeOrderView(ObjectActionAjaxView):
    """
    Представление: Изменение порядка поля
    """

    title = 'Изменение порядка поля'
    error_message = 'Групповые поля должны находиться перед остальными полями'
    join_errors = True
    model = ReportField

    def valid_action(self):
        # Отчет и новый порядковый номер
        report, new = self.object.report, int(self.request.POST.get('order'))

        # Количество групповых полей шаблона
        report_group_fields_count = report.report_fields.filter(is_group=True).count()
        if self.object.is_group:
            if new >= report_group_fields_count:
                self.add_error(self.error_message)
        else:
            if new < report_group_fields_count:
                self.add_error(self.error_message)
        return not bool(self._errors)

    def action(self):
        self.object.reorder(int(self.request.POST.get('order')))


class ReportFieldMixin:
    """
    Миксин полей шаблона
    """

    is_virtual = False
    model = ReportField
    template_name = 'report_designer/reports/processing_report_field.html'
    dependents = (('dynamic_contents', 'report_fields'),)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(is_virtual=self.is_virtual)
        return context_data


class ReportFieldUpdateView(ReportFieldMixin, UpdateAjaxView):
    """
    Представление: Редактирование полей отчета
    """

    title = 'Редактирование поля отчета'
    form_class = ReportFieldUpdateForm

    def get_title(self):
        return f'{super().get_title()} "{self.object.name}"'

    def before_save(self):
        super().before_save()
        self.group_field_next_order = self.object.report.group_field_next_order

    def after_save(self, **kwargs):
        super().after_save(**kwargs)
        form = kwargs.get('form')
        if 'is_group' in form.changed_data:
            self.object.reorder(self.group_field_next_order - int(not self.object.is_group))

    def set_object_additional_values(self, obj):
        super().set_object_additional_values(obj)
        if obj.is_group:
            obj.is_sort = True


# endregion Список полей в отчете


# region Списки для составления выражений


class ReportFunctionsDBTablesTreeListView(ExpressionsMixin, DBTablesBaseTreeListView):
    """
    Представление: Список таблиц в отчете
    """

    def get_queryset(self):
        # Доступны таблицы, добавленные в отчет
        return (
            super()
            .get_queryset()
            .for_report(self.parent)
            .filter(
                Q(
                    Q(pk=self.parent.root.pk),
                    Q(report_tables__report=self.parent, report_tables__relations__isnull=False),
                    _connector=Q.OR,
                )
            )
            .annotate(
                relation_name=F('report_tables__relations__name'),
                relation_count=Count('report_tables__relations'),
                relation_pk=F('report_tables__relations__pk'),
            )
        )


class FunctionsListView(AjaxResponseMixin, TemplateView):
    """
    Представление: список функций конструктора отчетов
    """

    template_name = 'report_designer/reports/blocks/functions_tree_branch.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(tree_branches=Functions.create_tree_for_template())
        return context_data


# endregion Списки для составления выражений


# region Виртуальные поля


class ReportVirtualFieldMixin(ParentMixin, ReportFieldMixin):
    """
    Миксин: Создание/Редактирование виртуального поля
    """

    is_virtual = True
    parent_model = Report
    kwargs_parent_fk = 'report_pk'
    form_class = ReportVirtualFieldCreateUpdateForm

    def set_object_additional_values(self, obj):
        super().set_object_additional_values(obj)
        if obj.is_group:
            obj.is_sort = True


class ReportVirtualFieldCreateView(ReportVirtualFieldMixin, CreateAjaxView):
    """
    Представление: Создание виртуального поля
    """

    title = 'Создание виртуального поля'

    def set_object_additional_values(self, obj):
        super().set_object_additional_values(obj)
        obj.report = self.parent
        obj.is_virtual = True
        obj.order = self.parent.field_next_order


class ReportVirtualFieldUpdateView(ReportVirtualFieldMixin, UpdateAjaxView):
    """
    Представление: Редактирование виртуального поля
    """

    title = 'Редактирование виртуального поля'


# endregion Виртуальные поля


class TableFieldsListSelect2View(ParentMixin, Select2BaseListView):
    """
    Загрузка полей select2
    """

    parent_model = Report
    queryset = TableField.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.table:
            return queryset.none()
        return (
            queryset.available_for_report(self.parent)
            .filter(db_table=self.table)
            .values()
            .annotate(name=Case(When(alias__exact='', then=F('name')), default=F('alias')))
            .distinct()
        )

    @cached_property
    def table(self):
        """
        Таблица
        """
        # Обработка родительской связи
        if 'relation' in self.request.GET:
            relation = self.request.GET.get('relation')
            if relation:
                relation = ReportTableRelation.objects.filter(report_table__report=self.parent, pk=relation).first()
                return relation.report_table.db_table if relation else None
            return self.parent.root

        # Обработка связываемой таблицы
        table = self.request.GET.get('table')
        if not table:
            return
        table = ReportTable.objects.filter(report=self.parent, pk=table).first()
        return table.db_table if table else None

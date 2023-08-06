from django.urls import path, include

from . import views


app_name = 'reports'


ajax_urls = [
    path('functions/', views.FunctionsListView.as_view(), name='functions'),
    path(
        '<int:report_pk>/functions/tables/',
        views.ReportFunctionsDBTablesTreeListView.as_view(),
        name='functions-tables',
    ),
    path('table/<str:type>/', views.ReportListView.as_view(), name='list'),
    path('create/', views.ReportCreateView.as_view(), name='create'),
    path('create_by_report/', views.ReportCreateByReportView.as_view(), name='create-by-report'),
    path('<int:pk>/update/', views.ReportUpdateView.as_view(), name='update'),
    path('<int:report_pk>/tables/<int:pk>/fields/', views.TableFieldsListView.as_view(), name='fields-list'),
    path('<int:report_pk>/tables/', views.DBTablesTreeListView.as_view(), name='tables-list'),
    path('<int:report_pk>/tables/included/', views.ReportDBTablesTreeListView.as_view(), name='included-tables-list'),
    path('<int:pk>/add_table/', views.ReportDBTableAddView.as_view(), name='add-table'),
    path('<int:pk>/remove_table/', views.ReportDBTableRemoveView.as_view(), name='remove-table'),
    path('<int:pk>/fields/<str:type>/', views.ReportFieldsListView.as_view(), name='report-fields-list'),
    path('fields/<int:pk>/delete/', views.ReportFieldsDeleteView.as_view(), name='report-fields-delete'),
    path(
        '<int:report_pk>/create_table_relations/',
        views.ReportTableRelationCreateView.as_view(),
        name='create-report-table-relation',
    ),
    path(
        '<int:report_pk>/table_relations/<int:pk>/update/',
        views.ReportTableRelationUpdateView.as_view(),
        name='update-report-table-relation',
    ),
    path(
        '<int:pk>/table_relations/<str:type>/',
        views.ReportTableRelationsListView.as_view(),
        name='report-table-relations-list',
    ),
    path('<int:pk>/add_fields/', views.ReportFieldsAddView.as_view(), name='add-fields'),
    path('<int:pk>/change_order/', views.ReportFieldChangeOrderView.as_view(), name='field-change-order'),
    path('<int:pk>/select2/fields/', views.TableFieldsListSelect2View.as_view(), name='select2-fields-list'),
    path(
        '<int:report_pk>/report_fields/create_virtual_field/',
        views.ReportVirtualFieldCreateView.as_view(),
        name='create-virtual-field',
    ),
    path('report_fields/<int:pk>/update/', views.ReportFieldUpdateView.as_view(), name='report-field-update'),
    path(
        '<int:report_pk>/report_fields/virtual/<int:pk>/update/',
        views.ReportVirtualFieldUpdateView.as_view(),
        name='report-virtual-field-update',
    ),
]


urlpatterns = [
    path('', views.ReportListView.as_view(), name='list', kwargs={'type': 'base'}),
    path('<int:pk>/', views.ReportDetailView.as_view(), name='detail'),
    path('generate/', views.ReportGenerateView.as_view(), name='generate'),
    path('ajax/', include(ajax_urls)),
]

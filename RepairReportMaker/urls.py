from django.urls import path
from RepairReportMaker import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('admin_index',views.admin_index),
    path('admin_edit',views.admin_edit),
    path('admin_form',views.admin_form),
    # path('edit/<int:pk>/',views.edit_department,name='edit_department'),
    # path('del/<int:pk>/',views.del_department,name='del_department'),
    path('edit2/<int:pk>/',views.edit_report,name='edit_report'),
    path('del2/<int:pk>/',views.del_report,name='del_report')
]
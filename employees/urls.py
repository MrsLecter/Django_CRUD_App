from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('employees/add', views.add_employee, name='employee_add'),
    path('employee/<str:pk>/', views.employee, name='employee'),
    path('employee/<str:pk>/put', views.update_employee, name='employee_update'),
    path('employee/<str:pk>/delete', views.delete_employee, name='employee_delete'),

    path('departments/', views.departments, name='departments'),
    path('department/<str:pk>/', views.department, name='department'),
    path('department/<str:pk>/put', views.update_department, name='department_update'),
    path('department/<str:pk>/delete', views.delete_department, name='department_delete'),
    path('departments/add/', views.add_department, name='department_add'),
]
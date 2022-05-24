from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('employees/add', views.add_employee, name='employee_add'),
    path('employee/<str:pk>/', views.employee, name='employee'),
    path('employee/<str:pk>/put', views.update_employee, name='employee_update'),

    path('departments/', views.departments, name='departments'),
    path('department/<str:pk>/', views.department, name='department'),
    path('departments/add/', views.add_department, name='department_add'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('departments/', views.departments, name='departments'),
    path('employee/<str:pk>/', views.employee, name='employee'),
    path('department/<str:pk>/', views.department, name='department'),
]
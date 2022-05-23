from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('employee/<str:pk>/', views.employee, name='employee')
]
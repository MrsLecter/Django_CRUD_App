from django.urls import path
from . import views

urlpatterns = [
    path('manager/', views.index, name='index'),
    path('project/<str:pk>/', views.project, name='project')
]
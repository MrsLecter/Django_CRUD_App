from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'manager.html')

def project(request):
    return render(request, 'single_project.html')
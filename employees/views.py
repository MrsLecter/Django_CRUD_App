from django.shortcuts import render

def employees(request):
    return render(request, 'employees.html')

def employee(request):
    return render(request, 'employee.html')
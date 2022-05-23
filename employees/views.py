from django.shortcuts import render
from employees.models import Employee, Deparment

def employees(request):
    data = Employee.objects.all()
    return render(request, 'employees.html', {'data':data})

def employee(request, pk):
    current_employee = Employee.objects.get(name=pk)
    return render(request, 'employee.html', {'data': current_employee})
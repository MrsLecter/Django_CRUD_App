from django.shortcuts import render
from employees.models import Employee, Deparment

def employees(request):
    data = Employee.objects.all()
    return render(request, 'employees.html', {'data':data})

def departments(request):
    data = Deparment.objects.all()
    return render(request, 'departments.html', {'data':data})

def employee(request, pk):
    current_employee = Employee.objects.get(name=pk)
    return render(request, 'employee.html', {'data': current_employee})

def department(request, pk):
    department_name = Deparment.objects.get(id=pk)
    employees = Employee.objects.filter(department=pk)
    return render(request, 'department.html', {'department': department_name, 'employee': employees})
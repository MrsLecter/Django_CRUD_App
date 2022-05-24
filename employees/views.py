# from certifi import contents
from django.shortcuts import render
from employees.models import Employee, Deparment
from .form import EmployeeForm, DepartmentForm

def employees(request):
    data = Employee.objects.all()
    return render(request, 'employees.html', {'data':data})

def employee(request, pk):
    current_employee = Employee.objects.get(name=pk)
    return render(request, 'employee.html', {'data': current_employee})

def add_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():   
            form.save()
    context = {'form': form}
    return render(request, 'modify_form.html', context)


def departments(request):
    data = Deparment.objects.all()
    return render(request, 'departments.html', {'data':data})

def department(request, pk):
    department_name = Deparment.objects.get(id=pk)
    employees = Employee.objects.filter(department=pk)
    return render(request, 'department.html', {'department': department_name, 'employee': employees})

def add_department(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():   
            form.save()
    context = {'form': form}
    return render(request, 'modify_form.html', context)
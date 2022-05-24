from django.shortcuts import render, redirect
from employees.models import Employee, Deparment
from .form import EmployeeForm, DepartmentForm

def employees(request):
    data = Employee.objects.all()
    return render(request, 'employee/employees.html', {'data':data})

def employee(request, pk):
    current_employee = Employee.objects.get(name=pk)
    return render(request, 'employee/employee.html', {'data': current_employee})

def add_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():   
            form.save()
        return redirect('employees')
    context = {'form': form}
    return render(request, 'modify_form.html', context)

def update_employee(request, pk):
    current_employee = Employee.objects.get(name=pk)
    form = EmployeeForm(instance=current_employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=current_employee)
        if form.is_valid():   
            form.save()
        return redirect('employees')
    context = {'form': form}
    return render(request, 'modify_form.html', context)

def delete_employee(request, pk):
    employee = Employee.objects.get(name=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees')
    context = {'object': employee}
    return render(request, 'emplayee/delete_form.html', context)



def departments(request):
    data = Deparment.objects.all()
    return render(request, 'department/departments.html', {'data':data})

def department(request, pk):
    department_name = Deparment.objects.get(id=pk)
    employees = Employee.objects.filter(department=pk)
    return render(request, 'department/department.html', {'department': department_name, 'employee': employees})

def add_department(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():   
            form.save()
        return redirect('departments')
    context = {'form': form}
    return render(request, 'modify_form.html', context)

def update_department(request, pk):
    current_department = Deparment.objects.get(id=pk)
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=current_department)
        if form.is_valid():   
            form.save()
        return redirect('departments')
    context = {'form': form}
    return render(request, 'modify_form.html', context)

def delete_department(request, pk):
    department = Deparment.objects.get(id=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('departments')
    context = {'object': department}
    return render(request, 'department/delete_form.html', context)
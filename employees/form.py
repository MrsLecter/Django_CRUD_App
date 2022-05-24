from dataclasses import field
from django.forms import ModelForm

# from employees.views import department
from .models import Employee, Deparment

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'age', 'phone', 'department']
    
class DepartmentForm(ModelForm):
    class Meta:
        model = Deparment
        fields = ['name']
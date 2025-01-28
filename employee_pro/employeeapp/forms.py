# app - forms.py

from django import forms  
from employeeapp.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  
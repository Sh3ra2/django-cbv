from django import forms
from .models import employeemodel

class employeemodelform(forms.ModelForm):
    class Meta:
        model =  employeemodel
        fields = ['name', 'address', 'occupation']
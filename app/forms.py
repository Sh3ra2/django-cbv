from django import forms
from .models import employeemodel, projectmodel, clientmodel

class employeemodelform(forms.ModelForm):
    class Meta:
        model =  employeemodel
        fields = '__all__'


class projectmodelform(forms.ModelForm):
    class Meta:
        model = projectmodel
        fields = '__all__'

class clientmodelform(forms.ModelForm):
    class Meta:
        model = clientmodel
        fields = '__all__'
from django import forms
from .models import employeeDetail

class employeeForms(forms.ModelForm):
    class Meta:
        model = employeeDetail
        fields = ["name","email","phone","hired_date","job_title","salary"]
        widgets = {"hired_date": forms.DateInput(attrs={"type": "date"})}

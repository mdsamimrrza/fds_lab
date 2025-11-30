from django import forms
from .models import studentCIE

class studentForms(forms.ModelForm):
    class Meta:
        model = studentCIE
        fields = ['usn', 'name','subject_code','cie_marks']
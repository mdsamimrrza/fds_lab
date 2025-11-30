from django import forms
from .models import examfeemodel

class examfeeforms(forms.ModelForm):
    class Meta:
        model = examfeemodel
        fields = ["name", "usn", "sem" , "exam_fee"]
from django import forms
from .models import GradeStudent


class GradeStudentForm(forms.ModelForm):
    class Meta:
        model = GradeStudent
        fields = ["name", "usn", "dept", "grade"]


class UpdateGradeForm(forms.Form):
    name = forms.CharField(max_length=100)
    new_grade = forms.CharField(max_length=2)

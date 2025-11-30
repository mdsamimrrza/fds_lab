from django import forms
from .models import ExamStudent


class ExamStudentForm(forms.ModelForm):
    class Meta:
        model = ExamStudent
        fields = ["name", "usn", "grade"]

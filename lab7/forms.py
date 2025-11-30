from django import forms
from .models import Faculty


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ["faculty_id", "title", "name", "branch"]

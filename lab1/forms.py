from django import forms
from .models import biodata

class boidataForm(forms.ModelForm):
    class Meta:
        model = biodata
        fields = ["name", "age", "email"]
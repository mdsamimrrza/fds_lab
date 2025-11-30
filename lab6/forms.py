from django import forms
from .models import Placement


class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ["usn", "name", "company_name"]

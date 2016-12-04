from django import forms
from . import models

class FilterForm(forms.Form):
    year=forms.ModelChoiceField(queryset=models.Year.objects.all(),required=False)
    country=forms.ModelChoiceField(queryset=models.Country.objects.all(),required=False)

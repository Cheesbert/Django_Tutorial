from django import forms
from .algorithm_methods import SortMethods # supports iteration

class SortForm(forms.Form):
    numbers = forms.CharField(
        label="Enter list of numbers for sorting (e.g. 5,3,7)",
        required=True
    )
    sort_methods = forms.MultipleChoiceField(
        choices=SortMethods.choices(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

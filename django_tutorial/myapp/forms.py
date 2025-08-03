from django import forms
from .algorithm_methods import SortMethods # supports iteration

class SortForm(forms.Form):
    user_input_list = forms.CharField(
        label="Enter list of numbers for sorting (e.g. 5,3,7)",
        required=False
    )
    sort_methods = forms.MultipleChoiceField(
        choices=SortMethods.choices(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    use_random_list = forms.BooleanField(
        label="Generate random list",
        required=False
    )
    list_range_min = forms.IntegerField(
        label="Minimum number",
        required=False
    )
    list_range_max = forms.IntegerField(
        label="Maximum number",
        required=False
    )
    list_length = forms.IntegerField(
        label="Length for list",
        required=False
    )


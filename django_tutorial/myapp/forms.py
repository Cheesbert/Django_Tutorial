from django import forms
from .algorithm_methods.sorting_methods import SortMethods # supports iteration

class SortForm(forms.Form):
    user_input_list = forms.CharField(
        label="Enter list of numbers for sorting (e.g. 1,3,7)",
        required=False,
        widget = forms.TextInput(attrs={"placeholder": "1,3,4"})
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

class GraphForm(forms.Form):
    user_node_input = forms.CharField(
        label="Enter node value (eg 1,3,4) which creates 3 nodes with given values",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "1,2,3"})
    )
    user_edge_start = forms.CharField(
        label="Enter start node (eg 1 for node1)",
        required=False,
        widget = forms.TextInput(attrs={"placeholder": "1"})
    )
    user_edge_end = forms.CharField(
        label="Enter end node (eg 2 for node2)",
        required=False,
        widget = forms.TextInput(attrs={"placeholder": "1,3,4"})
    )



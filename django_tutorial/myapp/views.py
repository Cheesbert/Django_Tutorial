import time
import numpy as np

from django.shortcuts import render, HttpResponse

from .forms import SortForm
from .models import TodoItem
from .algorithm_methods import SortMethods

# Create your views here.

def home(request):
    return render(request,"home.html")

def sorting_view(request):
    unsorted_list = None
    results = []

    if request.method == "POST":
        form = SortForm(request.POST)
        if form.is_valid():
            use_random_list = form.cleaned_data["use_random_list"]
            selected_methods = form.cleaned_data["sort_methods"]

            if use_random_list:
                list_range_min = form.cleaned_data["list_range_min"]
                list_range_max = form.cleaned_data["list_range_max"]
                list_length = form.cleaned_data["list_length"]

                if None in (list_length, list_range_min, list_range_max):
                    form.add_error(None, "List length, min and max are required for list generation")
                elif list_range_min > list_range_max or list_length <= 0:
                    form.add_error(None, "List length must be greater than 0 and min_range cannot be bigger than max_range")
                else: # valid input create list
                    unsorted_list = np.random.randint(list_range_min, list_range_max + 1, size=list_length).tolist()

            else: # User generated list
                user_input_list = form.cleaned_data["user_input_list"]
                try:
                    unsorted_list = [int(num.strip()) for num in user_input_list.split(",")]
                except ValueError:
                    form.add_error("user_input_list", "Invalid input. Use format: 5,3,7")

            if unsorted_list and len(unsorted_list) > 1:
                for method in selected_methods:
                    func = SortMethods.get_func(key=method)
                    start = time.perf_counter_ns()
                    sorted_list = func(unsorted_list)
                    end = time.perf_counter_ns()
                    results.append({
                        "method": method,
                        "sorted": sorted_list,
                        "time": f"{(end - start) / 1000} ms",
                    })

    else:
        form = SortForm()

    print(results)
    return render(request, 'sorting.html', {
        "form": form,
        "original_list": unsorted_list,
        "results": results
    })

def todos(request):
    items = TodoItem.objects.all
    return render(request, "todos.html", {"todos": items})

import time

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
            numbers = form.cleaned_data["numbers"]
            selected_methods = form.cleaned_data["sort_methods"]

            try:
                unsorted_list = [int(num.strip()) for num in numbers.split(",")]
                for method in selected_methods:
                    func = SortMethods.get_func(key=method)
                    start = time.perf_counter_ns()
                    sorted_list = func(unsorted_list)
                    print(sorted_list)
                    end = time.perf_counter_ns()
                    results.append({
                        "method": method,
                        "sorted": sorted_list,
                        "time": f"{(end - start) / 1000} ms",
                    })
            except ValueError:
                form.add_error("numbers", "wrong format")

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

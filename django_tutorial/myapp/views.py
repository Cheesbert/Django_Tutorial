import base64
import time
from datetime import datetime
from io import BytesIO

import numpy as np
import cv2 as cv

from django.shortcuts import render
from matplotlib import pyplot as plt

from .forms import SortForm, GraphForm
from .models import TodoItem
from .algorithm_methods.sorting_methods import SortMethods
from .data_structures.graph_types import GraphTypes



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
                else: # Valid input create list
                    unsorted_list = np.random.randint(list_range_min, list_range_max + 1, size=list_length).tolist()

            else: # User generated list
                user_input_list = form.cleaned_data["user_input_list"]
                try:
                    unsorted_list = [int(num.strip()) for num in user_input_list.split(",")]
                except ValueError:
                    form.add_error("user_input_list", "Invalid input. Use format: 5,3,7")

            if unsorted_list and len(unsorted_list) > 1:
                for method in selected_methods:
                    sort_func = SortMethods.get_func(key=method)
                    start = time.perf_counter_ns()
                    sorted_list = sort_func(unsorted_list)
                    end = time.perf_counter_ns()
                    results.append({
                        "method": method,
                        "sorted": sorted_list,
                        "time": f"{(end - start) / 1000} ms",
                    })

    else:
        form = SortForm()

    return render(request, 'sorting.html', {
        "form": form,
        "original_list": unsorted_list,
        "results": results
    })

def graph_view(request):
    graph_img = None
    node_input = None
    graph = None
    edge_start = None
    edge_end = None

    if request.method == "POST":
        form = GraphForm(request.POST)
        ##
        log_file = "debug_file.txt"
        log = {}
        ##

        if form.is_valid():
            node_input = form.cleaned_data["user_node_input"]
            edge_start = form.cleaned_data["user_edge_start"]
            edge_end = form.cleaned_data["user_edge_end"]
            graph_type = form.cleaned_data["user_graph_selection"]
            graph_cls = GraphTypes.get_graph_type(key=graph_type)
            graph = graph_cls()

        if node_input:
            node_values = [int(x.strip()) for x in node_input.split(',') if x.strip().isdigit()]
            log.update({"node_values" : node_values})
            for value in node_values:
                graph.add_node(value)

        if graph and edge_start and edge_end:
            try:
                graph.add_edge(int(edge_start), int(edge_end))
            except Exception as e:
                print("Edge error:", e)

        if graph:
            graph_img = graph.draw(format="base64")  # assumes graph has a draw() method using matplotlib
            with open("debug_file.txt", "w") as f:
                f.write(str(log))
    else:
        form = GraphForm()

    return render(request, "graph.html",
        {"form": form, "graph_img": graph_img}
    )


def todos(request):
    items = TodoItem.objects.all
    return render(request, "todos.html", {"todos": items})

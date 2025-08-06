from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sorting/", views.sorting_view, name="sorting"),
    path("graph/", views.graph_view, name="graph"),
    path("todos/", views.todos, name="Todos")
]

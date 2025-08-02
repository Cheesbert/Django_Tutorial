from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("algorithms/sorting/", views.sorting_view, name="sorting"),
    path("todos/", views.todos, name="Todos")

]

from enum import Enum
from django_tutorial.myapp.data_structure_implementations import graph


class GraphTypes(Enum):
    BASIC_GRAPH = ("basic_graph", "BasicGraph", graph.Graph)
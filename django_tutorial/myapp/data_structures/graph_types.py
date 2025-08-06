from enum import Enum
from ..data_structure_implementations import graph

class GraphTypes(Enum):
    BASIC_GRAPH = ("basic_graph", "BasicGraph", graph.Basic_Graph)

    def __init__(self, key, label, graph_type):
        self._key = key
        self.label = label
        self.graph_type = graph_type

    @property
    def value(self):
        return self._key

    @classmethod
    def choices(cls):
        return [(member.value, member.label) for member in cls]

    @classmethod
    def get_graph_type(cls, key):
        return {member.value: member.graph_type for member in cls}.get(key)
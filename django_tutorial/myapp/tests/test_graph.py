import unittest
import numpy as np
from numpy.ma.testutils import assert_equal
from myapp.data_structure_implementations.graph import Basic_Graph
class TestGraph(unittest.TestCase):
    def test_add_node(self):
        graph = Basic_Graph()
        graph.add_node(data=0)
        graph.add_node(1)

        self.assertEqual(graph.get_value(1), 1)
        self.assertDictEqual(graph.nodes, {0: 0, 1: 1})





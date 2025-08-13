import unittest
import numpy as np

from myapp.algorithm_methods import draw_shapes

class TestDrawShapes(unittest.TestCase):
    def test_distance(self):
        start = (0, 0)
        end = (100, 100)
        expected_distance = 100
        test_distance = draw_shapes.diagonal_distance(start, end)
        self.assertEqual(expected_distance, test_distance)


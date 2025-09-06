import unittest
import numpy as np
from numpy.ma.testutils import assert_equal

from myapp.constants import colors

from myapp.algorithm_methods import draw_shapes

class TestDrawShapes(unittest.TestCase):
    def test_distance(self):
        start = (0, 0)
        end = (100, 100)
        expected_distance = 100
        test_distance = draw_shapes.diagonal_distance(start, end)
        self.assertEqual(expected_distance, test_distance)


    def test_rectangle_outline(self):
        canvas = np.full((10, 10, 3), colors.WHITE)
        center = (5, 5)
        draw_shapes.draw_rectangle(canvas, center, size=10, color=colors.BLACK)
        # test if rec border pixels black
        np.testing.assert_equal(canvas[0, 0], colors.BLACK)
        np.testing.assert_equal(canvas[9, 9], colors.BLACK)
        np.testing.assert_equal(canvas[0, 9], colors.BLACK)
        np.testing.assert_equal(canvas[9, 0], colors.BLACK)


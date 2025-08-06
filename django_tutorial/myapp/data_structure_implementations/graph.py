import base64

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from PIL import Image
import io
from ..algorithm_methods.draw_shapes import rectangle
# from django_tutorial.myapp.algorithm_methods.draw_shapes import rectangle

class Node():
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def add_neighbor(self, node: "Node"):
        self.neighbors.append(node)


class Basic_Graph():
    def __init__(self):
        self.nodes = {}
        self.size = 1

    def add_node(self, data):
        self.nodes.update({self.size: Node(data)})
        self.size += 1

    def add_edge(self, key1, key2):
        node1 = self.nodes[key1]
        node2 = self.nodes[key2]
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

    def get_value(self, key):
        return self.nodes[key].data

    def draw(self, node_size=50, format="png"):
        canvas_size = len(self.nodes) * node_size
        canvas = np.ones((canvas_size, canvas_size))
        x = node_size
        y = node_size
        positions = {}

        for i, node in enumerate(self.nodes.values()):
            if x >= canvas_size:
                y += node_size * 2
                x = node_size

            positions[i+1] = (x, y)
            x += node_size * 2

        for key, pos in positions.items():
            rectangle(canvas, pos, node_size)
            cv.putText(canvas, f"{key}: {self.get_value(key)}", (pos[0] - 10, pos[1] + 5),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)


        if format == "base64":
            canvas_uint8 = np.clip(canvas * 255, 0, 255).astype(np.uint8)
            image = Image.fromarray(canvas_uint8)
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            return img_base64
        else:
            return canvas

if __name__ == '__main__':
    g = Basic_Graph()

    g.add_node(data=1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)

    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)

    img = g.draw(format="np.array")
    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
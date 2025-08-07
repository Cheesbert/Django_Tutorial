import heapq


def dijkstra_grid(array, start, end, free=1, node=0,):
    rows, cols = len(array), len(array[0])
    weight_empty = 1
    weight_node = 5

    distances = {} # length: path(list of coordinates)
    distance = 0
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]




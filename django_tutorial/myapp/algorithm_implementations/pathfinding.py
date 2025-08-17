import heapq
import queue
import numpy as np

from myapp.constants.colors import Color


def dijkstra_grid(array, start, end, free_color=Color.WHITE, node_color=Color.BLACK):
    rows, cols = len(array), len(array[0])
    weight_free = 1
    weight_node = 1000
    weight_path = 10

    visited = set()
    distances = {start: 0}
    previous = {}
    queue = [(0, start)]  # (distance, position)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current_distance, current_pos = heapq.heappop(queue)

        if current_pos in visited:
            continue
        visited.add(current_pos)

        if current_pos == end:
            break  # Found target

        row, col = current_pos

        for dr, dc in directions:
            nr, nc =  row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                field = array[nr][nc]

                if np.array_equal(field, free_color):
                    weight = weight_free
                elif np.array_equal(field, node_color):
                    weight = weight_node
                else:
                    weight = weight_path

                new_distance = current_distance + weight

                neighbor = (nr, nc)
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_pos
                    heapq.heappush(queue, (new_distance, neighbor))

    # Path reconstruction
    path = []
    current = end
    while current in previous:
        path.insert(0, current)
        current = previous[current]
    if path:
        path.insert(0, start)
    return path



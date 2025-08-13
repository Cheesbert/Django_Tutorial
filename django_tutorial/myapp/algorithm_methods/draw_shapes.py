import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from myapp.constants import colors

def circle_outline(canvas, center, radius, color=1, thickness=1):
    pass

def draw_arrow(canvas, front, back, color=colors.BLACK):
    vec_row = back[0] - front[0]
    vec_col = back[1] - front[1]
    length = np.hypot(vec_row, vec_col)

    if length == 0: return

    dir_row = vec_row / length
    dir_col = vec_col / length

    corner_pos90 = (
        front[0] + dir_row * length - dir_col * length,
        front[1] + dir_col * length + dir_row * length
    )
    corner_neg90 = (
        front[0] - dir_row * length + dir_col * length,
        front[1] + dir_col * length + dir_row * length
    )
    draw_line(canvas, front, corner_pos90, color)
    draw_line(canvas, front, corner_neg90, color)
    draw_line(canvas, corner_pos90, corner_neg90, color)


def draw_line(canvas, start, end, color):
    N = diagonal_distance(start, end)
    rows, cols = canvas.shape[:2]

    for i in range(N+1):
        t = 0.0 if N == 0 else i/N
        row, col = lerp(start, end, t)
        row = max(0, min(rows - 1, row))
        col = max(0, min(cols - 1, col))
        canvas[row, col] = color

def diagonal_distance(star, end):
    distance_row = abs(star[0] - end[0])
    distance_col = abs(star[1] - end[1])
    return round(max(distance_row, distance_col))

def lerp(start, end, t):
    row  = start[0] * (1-t) + end[0] * t
    col = start[1] * (1-t) + end[1] * t
    row, col = round(row), round(col)
    return row, col

def rectangle(canvas, center, size, color=1, thickness=1, outline=True):
    y, x = center[0], center[1]
    half = size // 2
    top = y - half
    bottom = y + half
    left = x - half
    right = x + half

    if outline:
        canvas[top:top + thickness, left:right] = color
        canvas[bottom - thickness:bottom, left:right] = color

        canvas[top:bottom, left:left + thickness] = color
        canvas[top:bottom, right - thickness:right] = color
    else:
        canvas[top:bottom, left:right] = color


if __name__ == '__main__':
    canvas = np.ones((100, 100), dtype=np.uint8) * 255  # white background
    draw_arrow(canvas, (50, 100), (50, 50))
    # center = (50, 50)
    # rectangle(canvas, center, size=10)
    #
    cv.imshow('canvas', canvas)
    cv.waitKey(0)
    cv.destroyAllWindows()


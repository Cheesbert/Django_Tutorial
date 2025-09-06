import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from myapp.constants.colors import Color


def circle_outline(canvas, center, radius, color=1, thickness=1):
    pass

def draw_arrow(canvas, front, back, color=Color.BLACK.rgb(), arrow_len=None, arrow_width=None):
    dr = front[0] - back[0]
    dc = front[1] - back[1]

    length = np.hypot(dr, dc)
    if length == 0:
        return

    if arrow_len is None:
        arrow_len = length//2
    if arrow_width is None:
        arrow_width = length//2

    ur, uc = dr / length, dc / length


    br = front[0] - arrow_len * ur
    bc = front[1] - arrow_len * uc

    # perpendicular
    pr, pc = -uc, ur

    left_corner = (int(br + pr * arrow_width/2), int(bc + pc * arrow_width/2))
    right_corner = (int(br - pr * arrow_width/2), int(bc - pc * arrow_width/2))

    draw_line(canvas, (int(front[0]), int(front[1])), left_corner, color)
    draw_line(canvas, (int(front[0]), int(front[1])), right_corner, color)
    draw_line(canvas, left_corner, right_corner, color)


def draw_line(canvas, start, end, color):
    N = diagonal_distance(start, end)
    rows, cols = canvas.shape[:2]

    for i in range(N + 1):
        t = 0.0 if N == 0 else i / N
        row, col = lerp(start, end, t)
        row = max(0, min(rows - 1, row))
        col = max(0, min(cols - 1, col))
        canvas[row, col] = color

def diagonal_distance(star, end):
    distance_row = abs(star[0] - end[0])
    distance_col = abs(star[1] - end[1])
    return max(distance_row, distance_col)

def lerp(start, end, t):
    row = start[0] * (1 - t) + end[0] * t
    col = start[1] * (1 - t) + end[1] * t
    row, col = round(row), round(col)
    return row, col


def draw_rectangle(canvas, center, size, color=1, thickness=1, outline=True):
    if thickness >= size:
        raise ValueError("Thickness cannot be bigger than size")

    row, col = center
    half = size // 2

    top = row - half
    bottom = row + half
    left = col - half
    right = col + half

    if outline:
        canvas[top:top + thickness, left:right] = color
        canvas[bottom - thickness:bottom, left:right] = color

        canvas[top:bottom, left:left + thickness] = color
        canvas[top:bottom, right - thickness:right] = color
    else:
        canvas[top:bottom, left:right] = color


if __name__ == '__main__':
    canvas = np.ones((100, 100), dtype=np.uint8) * 255  # white background
    # draw_arrow(canvas, (50, 100), (50, 50))
    center = (50, 50)
    draw_rectangle(canvas, center, size=10, thickness=1, outline=False)
    #
    cv.imshow('canvas', canvas)
    cv.waitKey(0)
    cv.destroyAllWindows()

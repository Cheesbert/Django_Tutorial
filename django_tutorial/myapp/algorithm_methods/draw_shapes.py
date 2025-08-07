import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def circle_outline(canvas, center, radius, color=1, thickness=1):
    pass

def rectangle(canvas, center, size, color=1, thickness=1, outline=True):
    x, y = center[0], center[1]
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
    center = (50, 50)
    rectangle(canvas, center, size=10)

    cv.imshow('canvas', canvas)
    cv.waitKey(0)
    cv.destroyAllWindows()


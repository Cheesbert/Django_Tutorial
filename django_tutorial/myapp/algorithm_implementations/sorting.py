"""
Quicksort Divide and Conquer

1 Choose pivot example middle elem

Elements before elems behind pivot
Same in subarrays

"""
import numpy as np

def bubblesort(data,):
    data = data.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def quicksort(data):
    data = data.copy()
    if len(data) <= 1:
        return data

    pivot = data[int(len(data)/2)]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot ]

    left = quicksort(left)
    right = quicksort(right)
    sorted = left + middle + right
    return sorted

def quicksort_inplace(data, start_idx=0, end_idx=None):
    if end_idx is None:
        end_idx = len(data) - 1

    if start_idx < end_idx:
        pivot_index = partition(data, start_idx, end_idx)
        quicksort_inplace(data, start_idx, pivot_index-1)
        quicksort_inplace(data, pivot_index+1, end_idx)

def partition(data, start_idx, end_idx):
    pivot = data[end_idx]
    i = start_idx - 1

    for j in range(start_idx, end_idx):
        if data[j] <= pivot:
            i+=1
            data[i], data[j] = data[j], data[i] # swap

    data

def heapify(data, n, i):
    head = i
    left = 2 * i + 1
    right = 2 * i +2

    if left < n and data[left] > data[head]:
        head = left

    if right < n and data[right] > data[head]:
        head = right

    if head != i:
        data[i], data[head] = data[head], data[i]
        heapify(data, n, head)

def heapsort(data):
    data = data.copy()
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, i ,0)

    return data

if __name__ == "__main__":
    data = np.array([2, 6, 1, 6, 8, 17, 13, 11, 33])
    print(quicksort(data))
""" merge sort module """


def sort(arr):
    """ merge sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if len(arr) == 0:
        return []

    mergesort(arr)

    return arr

def mergesort(arr):
    """ merge sort """

    step = 1
    while step <= len(arr) - 1:
        low = 0
        while low < len(arr) - 1:
            mid = low + step - 1
            high = min(mid + step, len(arr) - 1)
            merge(arr, low, mid, high)
            low += 2*step
        step *= 2

def merge(arr, low, mid, high):
    """ merge """

    left, right = arr[low:mid + 1], arr[mid + 1:high + 1]

    i, j, k = 0, 0, low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1

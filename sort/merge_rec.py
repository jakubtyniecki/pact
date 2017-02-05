""" merge rec sort module """

from sort.framework import validate

@validate
def sort(arr):
    """ merge rec sort """

    mergesort(arr)

    return arr

def mergesort(arr):
    """ merge rec sort """

    if len(arr) == 1:
        return

    mid = len(arr) >> 1

    left, right = arr[:mid], arr[mid:]

    mergesort(left)
    mergesort(right)

    merge(arr, left, right)

def merge(arr, left, right):
    """ merge """

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

""" merge rec sort module """


def sort(arr):
    """ merge rec sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if not arr:
        return []

    mergesort(arr)

    return arr

def mergesort(arr):
    """ merge rec sort """

    if len(arr) == 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

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

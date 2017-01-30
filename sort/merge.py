""" merge sort module """


def sort(arr):
    """ merge sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if not arr:
        return []

    mergesort(arr)

    return arr

def mergesort(arr):
    """ merge sort """

    step = 1
    while step <= len(arr) - 1:
        low = 0
        mid = low + step - 1
        while mid < len(arr) - 1:
            high = min(mid + step, len(arr) - 1)
            merge(arr, low, mid, high)
            low += 2*step
            mid = low + step - 1
        step *= 2

def merge(arr, low, mid, high):
    """ merge """

    assert low < len(arr) and mid < len(arr) and high < len(arr), \
        "low: {}, mid: {}, high: {}".format(low, mid, high)

    left, right = arr[low:mid + 1], arr[mid + 1:high + 1]

    i, j, k = 0, 0, low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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

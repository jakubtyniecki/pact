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
        first = 0
        mid = first + step

        while mid < len(arr):
            last = min(mid + step, len(arr))
            merge(arr, first, mid, last)
            first += step << 1
            mid = first + step

        step <<= 1

def merge(arr, first, mid, last):
    """ merge """

    assert first < len(arr) and mid < len(arr) and last <= len(arr), \
        "first: {}, mid: {}, last: {}".format(first, mid, last)

    left, right = arr[first:mid], arr[mid:last]

    i, j, k = 0, 0, first

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

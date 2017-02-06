""" merge sort module """

from sort.framework import validate

@validate
def sort(arr):
    """ merge sort """

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

    assert len(left) + len(right) <= len(arr), \
        "left: {}, right: {}, arr: {}".format(len(left), len(right), len(arr))

    i, j, k = 0, 0, first

    while i < len(left) and j < len(right):
        # merge items from both arrays into output in the right order
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    assert k <= len(arr)

    while i < len(left):
        # appaned what's left in the left array
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        # appaned what's left in the right array
        arr[k] = right[j]
        j += 1
        k += 1

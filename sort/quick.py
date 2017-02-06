""" quick sort module """

from sort.framework import validate

@validate
def sort(arr):
    """ quick sort """

    quicksort(arr, 0, len(arr) - 1)

    return arr

def quicksort(arr, first, last):
    """ quick sort """

    stack = []
    stack.append((first, last))

    while stack:
        pos = stack.pop()

        left, right = pos[0], pos[1]

        piv = partition(arr, left, right)

        if piv - 1 > left:
            stack.append((left, piv - 1))

        if piv + 1 < right:
            stack.append((piv + 1, right))

def partition(arr, first, last):
    """ partition """

    assert first < len(arr) and last < len(arr) and first < last, \
        "first: {}, last: {}".format(first, last)

    pivotindex = pivotpoint(first, last)

    if pivotindex > first:
        arr[first], arr[pivotindex] = arr[pivotindex], arr[first]

    pivotvalue = arr[first]

    left, right = first + 1, last

    while right >= left:
        while left <= right and arr[left] <= pivotvalue:
            left += 1

        while arr[right] >= pivotvalue and right >= left:
            right -= 1

        assert right >= 0 and left <= len(arr)

        if right > left:
            arr[left], arr[right] = arr[right], arr[left]

    if right > first:
        arr[first], arr[right] = arr[right], arr[first]

    return right

def pivotpoint(first, last):
    """ pivot point strategy
        using middle element
        to prevent worst case scenario """

    return first + (last - first) >> 1

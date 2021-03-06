""" quick rec sort module """

from sort.framework import validate

@validate
def sort(arr):
    """ quick rec sort """

    quicksort(arr, 0, len(arr) - 1)

    return arr

def quicksort(arr, first, last):
    """ quick rec sort """

    if first < last:
        splitpoint = partition(arr, first, last)

        sides = {"left": (first, splitpoint - 1), "right": (splitpoint + 1, last)}

        first_side, second_side = "left", "right"

        if last - splitpoint < splitpoint - first:
            # go with the smaller side first to save memory
            first_side, second_side = second_side, first_side

        quicksort(arr, sides[first_side][0], sides[first_side][1])
        quicksort(arr, sides[second_side][0], sides[second_side][1])

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
        using median of first, mid and last elements
        to prevent worst case scenario and
        overcome recursion max depth """

    return first + (last - first) >> 1

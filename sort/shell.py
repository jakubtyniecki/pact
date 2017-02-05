""" quick sort module """

from sort.framework import validate

@validate
def sort(arr):
    """ quick sort """

    shellsort(arr)

    return arr

def shellsort(arr):
    """ shell sort """

    count = len(arr) >> 1

    while count > 0:
        for start in range(count):
            gapsort(arr, start, count)

        count >>= 1

def gapsort(arr, start, gap):
    """ gap insertion sort """

    assert start + gap < len(arr), \
        "start: {}, gap: {}".format(start, gap)

    for i in range(start + gap, len(arr), gap):
        position, currentvalue = i, arr[i]

        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position -= gap

        arr[position] = currentvalue

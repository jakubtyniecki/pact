""" quick sort module """


def sort(arr):
    """ quick sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if not arr:
        return []

    shellsort(arr)

    return arr

def shellsort(arr):
    """ shell sort """

    sublistcount = len(arr) // 2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapsort(arr, startposition, sublistcount)

        sublistcount = sublistcount // 2

def gapsort(arr, start, gap):
    """ gap insertion sort """

    assert start + gap < len(arr), \
        "start: {}, gap: {}".format(start, gap)

    for i in range(start + gap, len(arr), gap):
        position, currentvalue = i, arr[i]

        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = currentvalue

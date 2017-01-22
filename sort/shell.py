""" quick sort module """


def sort(arr):
    """ quick sort """

    if arr is None:
        raise ValueError("input array is null")
    if len(arr) == 0:
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

    for i in range(start + gap, len(arr), gap):
        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = currentvalue

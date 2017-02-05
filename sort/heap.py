""" heap sort module """

from sort.framework import validate

@validate
def sort(arr):
    """ heap sort """

    heapsort(arr)

    return arr

def heapsort(arr):
    """ heap sort """

    heapify(arr)

    for i in [x for x in range(len(arr) - 1, 0, -1) if arr[0] > arr[x]]:
        arr[0], arr[i] = arr[i], arr[0]
        movedown(arr, 0, i - 1)

def heapify(arr):
    """ convert arr to heap """

    length = len(arr) - 1
    parent = length >> 1

    for i in range(parent, -1, -1):
        movedown(arr, i, length)

def movedown(arr, start, end):
    """ constraints heap """

    assert start < len(arr) and end < len(arr), \
        "start: {}, end: {}".format(start, end)

    root = start
    while (root << 1) + 1 <= end:
        child = (root << 1) + 1

        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break

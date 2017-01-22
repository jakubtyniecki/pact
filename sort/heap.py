""" heap sort module """


def sort(arr):
    """ heap sort """

    if arr is None:
        raise ValueError("input array is null")
    if len(arr) == 0:
        return []

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
    parent = length // 2

    for i in range(parent, -1, -1):
        movedown(arr, i, length)

def movedown(arr, start, end):
    """ constraints heap """

    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return
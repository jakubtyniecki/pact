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

    # convert arr to heap
    length = len(arr) - 1
    parent = length // 2

    for i in range(parent, -1, -1):
        movedown(arr, i, length)

    # flatten heap into sorted array
    for i in [x for x in range(length, 0, -1) if arr[0] > arr[x]]:
        arr[0], arr[i] = arr[i], arr[0]
        movedown(arr, 0, i - 1)

def movedown(arr, first, last):
    """ move down """

    largest = 2 * first + 1

    while largest <= last:
        # right child exists and is larger than left child
        if largest < last and arr[largest] < arr[largest + 1]:
            largest += 1

        # right child is larger than parent
        if arr[largest] > arr[first]:
            arr[first], arr[largest] = arr[largest], arr[first]
            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return

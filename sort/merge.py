""" merge sort module """


def sort(arr):
    """ merge sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if len(arr) == 0:
        return []

    mergesort(arr)

    return arr

def mergesort(arr):
    """ merge sort """
    if len(arr) == 1:
        return

    mid = len(arr) // 2

    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    mergesort(lefthalf)
    mergesort(righthalf)

    i, j, k = 0, 0, 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i = i + 1
        else:
            arr[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        arr[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        arr[k] = righthalf[j]
        j = j + 1
        k = k + 1

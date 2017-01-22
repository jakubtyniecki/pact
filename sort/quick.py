""" quick sort module """


def sort(arr):
    """ quick sort """

    if arr is None:
        raise ValueError("input array is null")
    if len(arr) == 0:
        return []

    quicksort(arr, 0, len(arr) - 1)

    return arr

def quicksort(arr, first, last):
    """ quick sort """
    if first < last:
        splitpoint = partition(arr, first, last)

        quicksort(arr, first, splitpoint - 1)
        quicksort(arr, splitpoint + 1, last)

def partition(arr, first, last):
    """ partition """
    pivotvalue = arr[first]

    leftmark, rightmark = first + 1, last

    done = False
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    arr[first], arr[rightmark] = arr[rightmark], arr[first]

    return rightmark

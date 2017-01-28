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

        wnd = [[first, splitpoint - 1], [splitpoint + 1, last]]

        if last - splitpoint < splitpoint - first:
            wnd[0], wnd[1] = wnd[1], wnd[0]

        quicksort(arr, wnd[0][0], wnd[0][1])
        quicksort(arr, wnd[1][0], wnd[1][1])

def partition(arr, first, last):
    """ partition """
    pivotindex = pivotpoint(first, last)
    arr[first], arr[pivotindex] = arr[pivotindex], arr[first]
    pivotvalue = arr[first]

    leftmark, rightmark = first + 1, last

    done = False
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    arr[first], arr[rightmark] = arr[rightmark], arr[first]

    return rightmark

def pivotpoint(first, last):
    """ pivot point strategy """
    return first + (last - first) // 2

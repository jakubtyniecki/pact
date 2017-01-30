""" quick rec sort module """


def sort(arr):
    """ quick rec sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if not arr:
        return []

    quicksort(arr, 0, len(arr) - 1)

    return arr

def quicksort(arr, first, last):
    """ quick rec sort """

    if first < last:
        splitpoint = partition(arr, first, last)

        wnd = [(first, splitpoint - 1), (splitpoint + 1, last)]

        if last - splitpoint < splitpoint - first:
            wnd[0], wnd[1] = wnd[1], wnd[0]

        quicksort(arr, wnd[0][0], wnd[0][1])
        quicksort(arr, wnd[1][0], wnd[1][1])

def partition(arr, first, last):
    """ partition """

    assert first < len(arr) and last < len(arr), \
        "first: {}, last: {}".format(first, last)

    pivotindex = pivotpoint(first, last)
    arr[first], arr[pivotindex] = arr[pivotindex], arr[first]
    pivotvalue = arr[first]

    left, right = first + 1, last

    done = False
    while not done:
        while left <= right and arr[left] <= pivotvalue:
            left += 1

        while arr[right] >= pivotvalue and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[first], arr[right] = arr[right], arr[first]

    return right

def pivotpoint(first, last):
    """ pivot point strategy """
    return first + (last - first) // 2

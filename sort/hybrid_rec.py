""" hybrid rec sort module """

def sort(arr):
    """ hybrid rec sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if not arr:
        return []

    hybridsort(arr, 0, len(arr) - 1)

    return arr

def hybridsort(arr, first, last):
    """ hybrid rec sort """

    if first < last:
        if last - first < 10:
            insertsort(arr, first, last)
        else:
            splitpoint = partition(arr, first, last)

            wnd = [(first, splitpoint - 1), (splitpoint + 1, last)]

            if last - splitpoint < splitpoint - first:
                wnd[0], wnd[1] = wnd[1], wnd[0]

            hybridsort(arr, wnd[0][0], wnd[0][1])
            hybridsort(arr, wnd[1][0], wnd[1][1])

def insertsort(arr, first, last):
    """ insert sort """

    assert first <= len(arr) and last < len(arr), \
        "first: {}, last: {}".format(first, last)

    for i in range(first, last + 1):
        position, currentvalue = i, arr[i]

        while position > 0 and arr[position - 1] > currentvalue:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = currentvalue

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

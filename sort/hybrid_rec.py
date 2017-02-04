""" hybrid rec sort module """

THRESHOLD = 10

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
        if last - first < THRESHOLD:
            insertsort(arr, first, last)
        else:
            splitpoint = partition(arr, first, last)

            sides = {"left": (first, splitpoint - 1), "right": (splitpoint + 1, last)}

            first_side, second_side = "left", "right"

            if last - splitpoint < splitpoint - first:
                first_side, second_side = second_side, first_side

            hybridsort(arr, sides[first_side][0], sides[first_side][1])
            hybridsort(arr, sides[second_side][0], sides[second_side][1])

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

    pivotindex = pivotpoint(arr, first, last)
    arr[first], arr[pivotindex] = arr[pivotindex], arr[first]
    pivotvalue = arr[first]

    left, right = first + 1, last

    while True:
        while left <= right and arr[left] <= pivotvalue:
            left += 1

        while arr[right] >= pivotvalue and right >= left:
            right -= 1

        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[first], arr[right] = arr[right], arr[first]

    return right

def pivotpoint(arr, first, last):
    """ pivot point strategy """
    mid = first + (last - first) // 2
    if (arr[first] - arr[mid]) * (arr[last] - arr[first]) >= 0:
        return first
    elif (arr[mid] - arr[first]) * (arr[last] - arr[mid]) >= 0:
        return mid
    else:
        return last

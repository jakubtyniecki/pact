""" hybrid sort module """

from sort.framework import validate

THRESHOLD = 10

@validate
def sort(arr):
    """ hybrid sort """

    hybridsort(arr, 0, len(arr) - 1)

    return arr

def hybridsort(arr, first, last):
    """ hybrid sort """

    stack = []
    stack.append((first, last))

    while stack:
        pos = stack.pop()

        left, right = pos[0], pos[1]

        if right - left < THRESHOLD:
            insertsort(arr, left, right)
        else:
            piv = partition(arr, left, right)

            if piv - 1 > left:
                stack.append((left, piv - 1))

            if piv + 1 < right:
                stack.append((piv + 1, right))

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

    if pivotindex > first:
        arr[first], arr[pivotindex] = arr[pivotindex], arr[first]

    pivotvalue = arr[first]

    left, right = first + 1, last

    while right >= left:
        while left <= right and arr[left] <= pivotvalue:
            left += 1

        while arr[right] >= pivotvalue and right >= left:
            right -= 1

        if right > left:
            arr[left], arr[right] = arr[right], arr[left]

    if right > first:
        arr[first], arr[right] = arr[right], arr[first]

    return right

def pivotpoint(arr, first, last):
    """ pivot point strategy """

    mid = first + (last - first) >> 1

    if (arr[first] - arr[mid]) * (arr[last] - arr[first]) >= 0:
        return first
    elif (arr[mid] - arr[first]) * (arr[last] - arr[mid]) >= 0:
        return mid
    else:
        return last

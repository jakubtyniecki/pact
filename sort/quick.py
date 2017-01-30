""" quick sort module """


def sort(arr):
    """ quick sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if len(arr) == 0:
        return []

    quicksort(arr, 0, len(arr) - 1)

    return arr

def quicksort(arr, first, last):
    """ quick sort """
    stack = []
    stack.append((first, last))

    while stack:
        pos = stack.pop()

        left, right = pos[0], pos[1]

        piv = partition(arr, left, right)

        if piv - 1 > left:
            stack.append((left, piv - 1))

        if piv + 1 < right:
            stack.append((piv + 1, right))

def partition(arr, first, last):
    """ partition """
    pivotindex = pivotpoint(first, last)
    arr[first], arr[pivotindex] = arr[pivotindex], arr[first]
    pivotvalue = arr[first]

    left, right = first + 1, last

    done = False
    while not done:
        while left <= right and arr[left] <= pivotvalue:
            left = left + 1

        while arr[right] >= pivotvalue and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[first], arr[right] = arr[right], arr[first]

    return right

def pivotpoint(first, last):
    """ pivot point strategy """
    return first + (last - first) // 2

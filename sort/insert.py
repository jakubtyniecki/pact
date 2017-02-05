""" insert sort module """

from sort.framework import validate

@validate
def sort(arr):
    """ insert sort """

    insertsort(arr)

    return arr

def insertsort(arr):
    """ insert sort """

    for i in range(1, len(arr)):
        position, currentvalue = i, arr[i]

        while position > 0 and arr[position - 1] > currentvalue:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = currentvalue

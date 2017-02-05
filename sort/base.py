""" base sort module """

from sort.framework import validate

@validate
def sort(arr):
    """ base sort """

    return sorted(arr)

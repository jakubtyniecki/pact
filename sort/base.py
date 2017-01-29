""" base sort module """


def sort(arr):
    """ base sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if len(arr) == 0:
        return []

    return sorted(arr)

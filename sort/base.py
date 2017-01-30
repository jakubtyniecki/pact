""" base sort module """


def sort(arr):
    """ base sort """

    if arr is None:
        raise TypeError("'NoneType' object is not iterable")
    if not arr:
        return []

    return sorted(arr)

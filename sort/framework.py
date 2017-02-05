
""" framework """

def validate(func):
    """ verify """

    def inner(arr):
        """ inner """

        if arr is None:
            raise TypeError("'NoneType' object is not iterable")
        if not arr:
            return []

        return func(arr)
    return inner

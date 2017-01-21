""" array sort module """


def array_sort(a, s=None):
    """ array sort """
    if s is None:
        s = sorted
    return s(a)

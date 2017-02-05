
""" helper """

def is_sorted(arr):
    """ assert array is sorted """

    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

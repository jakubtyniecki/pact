""" insert sort performance tests module """

import random
import timeit

repeat_count = 10
arr_count = {
    "small": 10,
    "medium": 100,
    "large": 1000
}
random_arr = {
    "small": [],
    "medium": [],
    "large": []
}
results = {
    "small": .0,
    "medium": .0,
    "large": .0
}

def init():
    for key in random_arr.keys():
        random_arr[key] = random.sample(range(arr_count[key]), arr_count[key])

def test(sut):
    for key in random_arr.keys():
        action = lambda k=key: sut.sort(random_arr[k])
        results[key] = timeit.timeit(action, number=repeat_count)

def execute(sort):
    init()
    test(sort)
    return results

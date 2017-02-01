""" insert sort performance tests module """

import random
import timeit

TESTS_SHORT_COUNT = 10
TESTS_SHORT = {
    "small": 10,
    "medium": 300,
    "large": 1500
}

def execute_short(sut):
    """ execute """
    results = {}
    for key in TESTS_SHORT.keys():
        test_arr = random.sample(range(TESTS_SHORT[key]), TESTS_SHORT[key])
        action = lambda arr=test_arr: sut.sort(arr[:])
        results[key] = "{:0.5f}".format(timeit.timeit(action, number=TESTS_SHORT_COUNT))
    return results

TESTS_LONG_COUNT = 1
TESTS_LONG_NUM = 8

def gen(val):
    """ gen """
    i = 8
    for current in range(val + 1):
        yield i
        i <<= 1

def execute_long(sut):
    """ execute """
    results = []
    for num in gen(TESTS_LONG_NUM):
        test_arr = random.sample(range(num), num)
        action = lambda arr=test_arr: sut.sort(arr[:])
        results.append(timeit.timeit(action, number=TESTS_LONG_COUNT) * 10)
    return results

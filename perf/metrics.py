""" insert sort performance tests module """

import random
import timeit

TESTS_COUNT = 10
TESTS = {
    "small": 10,
    "medium": 300,
    "large": 1500
}

def execute(sut):
    """ execute """
    results = {}
    for key in TESTS.keys():
        test_arr = random.sample(range(TESTS[key]), TESTS[key])
        action = lambda arr=test_arr: sut.sort(arr[:])
        results[key] = "{:0.5f}".format(timeit.timeit(action, number=TESTS_COUNT))
    return results


""" insert sort performance tests module """

import random
import timeit

TESTS_SHORT = {
    "timeit_count": 10,
    "range": {
        "small": {
            "max_len": 10
        },
        "medium": {
            "max_len": 300
        },
        "large": {
            "max_len": 1500
        }
    }
}

def get_variance(rng, variance):
    """ get variance """

    return {
        'small': 10,
        'medium': TESTS_SHORT["range"][rng]["max_len"] // 3,
        'large': TESTS_SHORT["range"][rng]["max_len"]
    }[variance]

def get_array(variance, max_len):
    """ get array """

    return [random.randint(1, variance) for _ in range(max_len)]

def execute_short(sut, variance):
    """ execute short """

    results = {}

    for rng in TESTS_SHORT["range"].keys():
        var = get_variance(rng, variance)
        max_len = TESTS_SHORT["range"][rng]["max_len"]
        test_arr = get_array(var, max_len)
        action = lambda arr=test_arr: sut.sort(arr[:])
        results[rng] = "{:0.5f}".format(timeit.timeit(action, number=TESTS_SHORT["timeit_count"]))

    return results

TESTS_PLOT = {
    "timeit_count": 1,
    "range": {
        "small": {
            "step": 10,
            "max_len": 500
        },
        "medium": {
            "step": 30,
            "max_len": 1500
        },
        "large": {
            "step": 100,
            "max_len": 5000
        }
    }
}

def gen_arrays(rng):
    """ gen arrays """

    step = TESTS_PLOT["range"][rng]["step"]
    max_len = TESTS_PLOT["range"][rng]["max_len"]

    for i in range(step, max_len, step):
        yield i

def execute_plot(sut, rng, variance):
    """ execute plot """

    results = []
    var = get_variance(rng, variance)

    for max_len in gen_arrays(rng):
        test_arr = get_array(var, max_len)
        action = lambda arr=test_arr: sut.sort(arr[:])
        results.append(timeit.timeit(action, number=TESTS_PLOT["timeit_count"]))

    return results

""" insert sort performance tests module """

import random
import timeit
from sort import insert

class InsertSortPerfTests():
    """ insert sort performance tests class """
    repeat_count = 100
    arr_count = {
        "small": 10,
        "medium": 100,
        "large": 10000
    }
    random_arr = {
        "small": [],
        "medium": [],
        "large": []
    }

    def init(self):
        """ setting up for tests """
        for key in self.random_arr.keys():
            self.random_arr[key] = random.sample(range(self.arr_count[key]), self.arr_count[key])

    def clean(self):
        """ cleaning up after tests """
        del self.random_arr

    def sort_small(self):
        """ should sort a small random array """
        print(timeit.timeit('insert.sort(self.random_arr["small"])', self.repeat_count))

    def execute(self):
        """ execute tests """
        self.init()
        self.sort_small()
        self.clean()

if __name__ == "__main__":
    InsertSortPerfTests().execute()

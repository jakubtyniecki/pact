""" insert sort tests module """

import unittest
import random
from sort import insert

class InsertSortTests(unittest.TestCase):
    """ insert sort unit tests class """
    max = 100
    arr = []

    def setUp(self):
        """ setting up for the test """
        #self.arr = random.sample(range(self.max), self.max)

    def tearDown(self):
        """ cleaning up after the test"""
        #del self.arr

    # def is_sorted(self, arr):
    #     """ assert array is sorted """
    #     return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

    def test_sort(self):
        """ should sort a given array """
        res = insert.sort(self.arr)
        #self.assertTrue(self.is_sorted(res))
        self.assertTrue(all(res[i] <= res[i+1] for i in range(len(res)-1)))

suite = unittest.TestLoader().loadTestsFromTestCase(InsertSortTests)
unittest.TextTestRunner(verbosity=2).run(suite)

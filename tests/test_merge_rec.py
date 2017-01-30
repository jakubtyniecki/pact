

""" merge rec sort tests module """

import unittest
import random

from sort import merge_rec

class MergeSortTests(unittest.TestCase):
    """ merge rec sort unit tests class """
    max = 100
    arr = []

    def setUp(self):
        """ setting up for the test """
        self.arr = random.sample(range(self.max), self.max)

    def tearDown(self):
        """ cleaning up after the test"""
        pass

    def is_sorted(self, arr):
        """ assert array is sorted """
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

    def test_null_input(self):
        """ should raise when input array is None """
        # arrange
        inp = None
        # act
        with self.assertRaises(TypeError) as ex:
            merge_rec.sort(inp)
        # assert
        self.assertEqual("'NoneType' object is not iterable", str(ex.exception))

    def test_empty_input(self):
        """ should return [] when input array is empty """
        # arrange
        inp = []
        # act
        res = merge_rec.sort(inp)
        # assert
        self.assertEqual(len(inp), len(res))

    def test_sort_a_given_array(self):
        """ should sort a given array """
        # act
        res = merge_rec.sort(self.arr[:])
        # assert
        self.assertTrue(self.is_sorted(res))

if __name__ == '__main__':
    unittest.main()

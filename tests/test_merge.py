
""" merge sort tests module """

import unittest
import random

from sort import merge
from tests import helper

class MergeSortTests(unittest.TestCase):
    """ merge sort unit tests class """
    max = 100
    arr = []

    def setUp(self):
        """ setting up for the test """
        self.arr = random.sample(range(self.max), self.max)

    def test_null_input(self):
        """ should raise when input array is None """
        # arrange
        inp = None

        # act
        with self.assertRaises(TypeError) as ex:
            merge.sort(inp)

        # assert
        self.assertEqual("'NoneType' object is not iterable", str(ex.exception))

    def test_empty_input(self):
        """ should return [] when input array is empty """
        # arrange
        inp = []

        # act
        res = merge.sort(inp)

        # assert
        self.assertEqual(len(inp), len(res))

    def test_sort_a_given_array(self):
        """ should sort a given array """
        # act
        res = merge.sort(self.arr[:])

        # assert
        self.assertTrue(helper.is_sorted(res))

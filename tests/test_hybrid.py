
""" hybrid sort tests module """

import unittest
import random

from tests import helper
from sort import hybrid

class HybridSortTests(unittest.TestCase):
    """ hybrid sort unit tests class """
    max = 20
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
            hybrid.sort(inp)
        # assert
        self.assertEqual("'NoneType' object is not iterable", str(ex.exception))

    def test_empty_input(self):
        """ should return [] when input array is empty """
        # arrange
        inp = []
        # act
        res = hybrid.sort(inp)
        # assert
        self.assertEqual(len(inp), len(res))

    def test_sort_a_given_array(self):
        """ should sort a given array """
        # act
        res = hybrid.sort(self.arr[:])
        # assert
        self.assertTrue(helper.is_sorted(res))

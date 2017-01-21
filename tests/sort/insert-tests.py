""" insert sort tests module """

import unittest

import array_sort from sort


class InsertSortTests(unittest.TestCase):
    """ insert sort tests class """

    def test(self):
        a = []
        array_sort(a, insert_sort)

suite = unittest.TestLoader().loadTestsFromTestCase(InsertSortTests)
unittest.TextTestRunner(verbosity=2).run(suite)

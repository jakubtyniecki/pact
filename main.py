""" main """

from sort import insert

def main():
    """ main """
    arr = [3, 1, 2]
    res = insert.sort(arr)
    print(res)

main()

#suite = unittest.TestLoader().loadTestsFromTestCase(InsertSortTests)
#unittest.TextTestRunner(verbosity=2).run(suite)

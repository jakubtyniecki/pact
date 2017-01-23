""" main """

import pprint

from perf import metrics
from sort import insert, shell, merge, heap, quick

def main():
    """ main """
    results = {}

    results["insert"] = metrics.execute(insert)
    results["shell"] = metrics.execute(shell)
    results["merge"] = metrics.execute(merge)
    results["heap"] = metrics.execute(heap)
    results["quick"] = metrics.execute(quick)

    print("{}\t{}\t{}\t{}".format("", "small", "medium", "large"))
    for key in results.keys():
        print("{}\t{}\t{}\t{}".format(key, \
            results[key]["small"], results[key]["medium"], results[key]["large"]))

main()

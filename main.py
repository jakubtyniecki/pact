""" main """

import numpy as np
from matplotlib import pyplot as plt

from perf import metrics
from sort import base, insert, shell, merge_rec, merge, heap, quick_rec, quick, hybrid_rec, hybrid

#import random

def main():
    """ main """

    # arr = random.sample(range(30), 30)
    # print(arr)

    # res = hybrid.sort(arr[:])
    # print(res)

    results = {}

    results["base"] = metrics.execute_short(base)
    results["insert"] = metrics.execute_short(insert)
    results["shell"] = metrics.execute_short(shell)
    results["merge (rec)"] = metrics.execute_short(merge_rec)
    results["merge"] = metrics.execute_short(merge)
    results["heap"] = metrics.execute_short(heap)
    results["quick (rec)"] = metrics.execute_short(quick_rec)
    results["quick"] = metrics.execute_short(quick)
    results["hybrid (rec)"] = metrics.execute_short(hybrid_rec)
    results["hybrid"] = metrics.execute_short(hybrid)

    print("{name: <15}\t{}\t{}\t{}".format("small", "medium", "large", name=""))
    for key in sorted(results.keys()):
        print("{name: <15}\t{}\t{}\t{}".format(\
            results[key]["small"], results[key]["medium"], results[key]["large"], name=key))

    results["base"] = metrics.execute_long(base)
    results["insert"] = metrics.execute_long(insert)
    results["shell"] = metrics.execute_long(shell)
    results["merge (rec)"] = metrics.execute_long(merge_rec)
    results["merge"] = metrics.execute_long(merge)
    results["heap"] = metrics.execute_long(heap)
    results["quick (rec)"] = metrics.execute_long(quick_rec)
    results["quick"] = metrics.execute_long(quick)
    results["hybrid (rec)"] = metrics.execute_long(hybrid_rec)
    results["hybrid"] = metrics.execute_long(hybrid)

    exes = [x for x in metrics.gen(metrics.TESTS_LONG_NUM)]
    fig, ax = plt.subplots()
    #ax.set_xscale('log', basex=2)
    ax.set_yscale('log', basey=2)
    for key in sorted(results.keys()):
        plt.plot(exes, results[key], label=key)

    plt.title("Comparison of sorting algorithms")
    plt.xlabel("number of elements")
    plt.ylabel("time elapsed (seconds)")
    plt.legend(loc='upper left')
    plt.show()

main()

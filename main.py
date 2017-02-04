""" main """

#import random

import numpy as np
from matplotlib import pyplot as plt

from perf import metrics
from sort import base, insert, shell, merge_rec, merge, heap, quick_rec, quick, hybrid_rec, hybrid

def main():
    """ main """

    # arr = [random.randint(1, 10) for _ in range(30)]
    # print(arr)

    # res = hybrid.sort(arr[:])
    # print(res)

    # tests_short = [
    #     base, insert, shell, merge_rec, merge, heap, quick_rec, quick, hybrid_rec, hybrid
    # ]

    # print("{name: <15}\t{}\t{}\t{}".format("small", "medium", "large", name=""))
    # for sut in sorted(tests_short, key=lambda s: s.__name__):
    #     result = metrics.execute_short(sut, "large")
    #     print("{name: <15}\t{}\t{}\t{}".format(\
    #         result["small"], result["medium"], result["large"], name=sut.__name__))

    tests_long = [
        base, insert, shell, merge_rec, merge, heap, quick_rec, quick, hybrid_rec, hybrid
    ]

    exes = [x for x in metrics.gen_arrays("large")]
    fig, ax = plt.subplots()
    #ax.set_xscale('log', basex=2)
    ax.set_yscale('log', basey=2)
    for sut in sorted(tests_long, key=lambda s: s.__name__):
        result = metrics.execute_long(sut, "large", "large")
        color = None
        linestyle = None
        linewidth = None
        if "rec" in sut.__name__:
            linestyle = '--'
        if "base" in sut.__name__:
            color = 'k'
            linestyle = ':'
            linewidth = 3.0
        if "hybrid" in sut.__name__:
            color = 'k'
            linewidth = 2.0
        plt.plot(exes, result, \
            color=color, linestyle=linestyle, linewidth=linewidth, label=sut.__name__)

    plt.title("Comparison of sorting algorithms")
    plt.xlabel("number of elements")
    plt.ylabel("time elapsed (seconds)")
    plt.legend(loc='upper left')
    plt.show()

main()

""" main """

#import random

import argparse

from matplotlib import pyplot as plt

from perf import metrics
from sort import base, insert, shell, merge_rec, merge, heap, quick_rec, quick, hybrid_rec, hybrid

TESTS = [
    base, insert, shell, merge_rec, merge, heap, quick_rec, quick, hybrid_rec, hybrid
]

def short_metrics(variance):
    """ short metrics """

    print("{name: <15}\t{}\t{}\t{}".format("small", "medium", "large", name=""))
    for sut in sorted(TESTS, key=lambda s: s.__name__):
        result = metrics.execute_short(sut, variance)
        print("{name: <15}\t{}\t{}\t{}".format(\
            result["small"], result["medium"], result["large"], name=sut.__name__))

def get_style(sut_name):
    """ get style """
    color = None
    linestyle = None
    linewidth = None
    if "rec" in sut_name:
        linestyle = '--'
    if "base" in sut_name:
        color = 'k'
        linestyle = ':'
        linewidth = 3.0
    if "hybrid" in sut_name:
        color = 'k'
        linewidth = 2.0
    return (color, linestyle, linewidth)

def get_tests(tests, fltr):
    """ get tests """
    cmp = lambda x: True
    if "rec" in fltr:
        cmp = lambda x: "rec" in x
    else:
        if "iter" in fltr:
            cmp = lambda x: "rec" not in x
    return sorted(
        [x for x in tests if "base" in x.__name__ or cmp(x.__name__)], \
        key=lambda s: s.__name__)

def plot_metrics(rng, variance, fltr):
    """ plot metrics """

    exes = [x for x in metrics.gen_arrays(rng)]
    fig, ax = plt.subplots()
    #ax.set_xscale('log', basex=2)
    ax.set_yscale('log', basey=2)
    for sut in get_tests(TESTS, fltr):
        result = metrics.execute_long(sut, rng, variance)
        color, linestyle, linewidth = get_style(sut.__name__)
        plt.plot(exes, result, \
            color=color, linestyle=linestyle, linewidth=linewidth, label=sut.__name__)

    plt.title("Comparison of sorting algorithms")
    plt.xlabel("number of elements")
    plt.ylabel("time elapsed (seconds)")
    plt.legend(loc='upper left')
    plt.show()

def main():
    """ main """

    parser = argparse.ArgumentParser(description='PACT arguments.')

    parser.add_argument('-metrics', choices=['short', 'plot'], default="short")
    parser.add_argument('-range', choices=['small', 'medium', 'large'], default="small")
    parser.add_argument('-variance', choices=['small', 'medium', 'large'], default="large")
    parser.add_argument('-filter', choices=['all', 'iter', 'rec'], default="all")

    args = parser.parse_args()

    if args.metrics == "short":
        short_metrics(args.variance)

    if args.metrics == "plot":
        plot_metrics(args.range, args.variance, args.filter)

main()

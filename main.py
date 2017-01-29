""" main """

from perf import metrics
from sort import base, insert, shell, merge, heap, quick_rec

#import random

def main():
    """ main """

    # arr = random.sample(range(20), 20)
    # print(arr)

    # res = quick.sort(arr[:])
    # print(res)

    results = {}

    results["base"] = metrics.execute(base)
    results["insert"] = metrics.execute(insert)
    results["shell"] = metrics.execute(shell)
    results["merge"] = metrics.execute(merge)
    results["heap"] = metrics.execute(heap)
    results["quick (rec)"] = metrics.execute(quick_rec)

    print("{name: <15}\t{}\t{}\t{}".format("small", "medium", "large", name=""))
    for key in sorted(results.keys()):
        print("{name: <15}\t{}\t{}\t{}".format(\
            results[key]["small"], results[key]["medium"], results[key]["large"], name=key))

main()

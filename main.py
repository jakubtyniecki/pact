""" main """

from perf import metrics
from sort import base, insert, shell, merge_rec, merge, heap, quick_rec, quick, hybrid_rec, hybrid

import random

def main():
    """ main """

    # arr = random.sample(range(30), 30)
    # print(arr)

    # res = hybrid.sort(arr[:])
    # print(res)

    results = {}

    results["base"] = metrics.execute(base)
    results["insert"] = metrics.execute(insert)
    results["shell"] = metrics.execute(shell)
    results["merge (rec)"] = metrics.execute(merge_rec)
    results["merge"] = metrics.execute(merge)
    results["heap"] = metrics.execute(heap)
    results["quick (rec)"] = metrics.execute(quick_rec)
    results["quick"] = metrics.execute(quick)
    results["hybrid (rec)"] = metrics.execute(hybrid_rec)
    results["hybrid"] = metrics.execute(hybrid)

    print("{name: <15}\t{}\t{}\t{}".format("small", "medium", "large", name=""))
    for key in sorted(results.keys()):
        print("{name: <15}\t{}\t{}\t{}".format(\
            results[key]["small"], results[key]["medium"], results[key]["large"], name=key))

main()

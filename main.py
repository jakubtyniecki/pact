""" main """

from perf import metrics

from sort import insert, shell, merge, heap, quick

results = {
    "insert": {},
    "shell": {},
    "merge": {},
    "heap": {},
    "quick": {}
}

def main():
    """ main """
    results["insert"] = metrics.execute(insert)
    results["shell"] = metrics.execute(shell)
    results["merge"] = metrics.execute(merge)
    results["heap"] = metrics.execute(heap)
    results["quick"] = metrics.execute(quick)

    print(results)

    # print("\t")
    # for key in results.keys():
    #     print("{0:s}\t".format(key))

    # for set_key in ["small", "medium", "large"]:
    #     for key in results.keys():
    #         print("{0}\t{1:.5f}\t".format(set_key, results[key][set_key]))

main()

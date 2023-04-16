import shelve
import time
from collections import defaultdict

from cache.cache import Cache
from cache.fifo import Fifo
from cache.fwf import Fwf
from cache.lfu import Lfu
from cache.lru import Lru
from cache.rand import Rand
from cache.rma import Rma
from distributions import get_sample

no_experiments = 1000
n_values = [*range(20, 110, 10)]
# dividend = [*range(10, 4, -1)]
# dividend = [*range(10, 9, -1)]
distributions = ["uniform", "geometric", "harmonic", "snd_harmonic"]
algorithms = ["fifo", "fwf", "lru", "lfu", "rand", "rma"]
# algorithms = ["fifo"]


def get_cache(algorithm: str, k: int) -> Cache:
    match algorithm:
        case "fifo":
            return Fifo(k)
        case "fwf":
            return Fwf(k)
        case "lru":
            return Lru(k)
        case "lfu":
            return Lfu(k)
        case "rand":
            return Rand(k)
        case "rma":
            return Rma(k)


def calc_avg_getting_page_cost(distribution: str, algorithm: str, k: int, n: int, size=2500) -> float:
    sample = get_sample(distribution=distribution, n=n, size=size)
    cache = get_cache(algorithm=algorithm, k=k)

    faults_num = 0
    for page in sample:
        faults_num += cache.get_page(page=page)

    return faults_num / size


# def experiment():
#     for dist in distributions:
#         print(f"\n{dist}")
#
#         avg_cost = defaultdict(dict)
#         for d in dividend:
#             print(f"\n\td={d}", end="")
#             avg_cost[d] = defaultdict(dict)
#
#             for algorithm in algorithms:
#                 print(f"\n\t\t{algorithm}", end=" ")
#                 for n in n_values:
#                     print(f"\t\t{n}", end=" ")
#                     c = 0
#                     for i in range(no_experiments):
#                         c += calc_avg_getting_page_cost(distribution=dist, algorithm=algorithm, n=n, k=round(n / d))
#                     avg_cost[d][algorithm][n] = c / no_experiments
#
#         with shelve.open('result') as db:
#             db[dist] = avg_cost


def experiment():
    for dist in distributions:
        print(f"\n{dist}")

        for n in n_values:
            print(f"\n\t{n}", end=" ")
            avg_cost = defaultdict(dict)

            for algorithm in algorithms:
                print(f"\t{algorithm}", end=" ")

                for k in range(n//10, n//5 + 1):
                    print(f"{k}", end="")
                    c = 0
                    ti = time.time()
                    for i in range(no_experiments):
                        c += calc_avg_getting_page_cost(distribution=dist, algorithm=algorithm, k=k, n=n)
                    print(" (", time.time() - ti, ")", end=" ")
                    avg_cost[algorithm][k] = c / no_experiments

            with shelve.open(f'results/{dist}_n{n}') as db:
                db['results'] = avg_cost


if __name__ == '__main__':
    experiment()

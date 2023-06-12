import shelve
from collections import Counter

from algorithms import move_to_min, flip
from distances import hypercube_distance, torus_distance
from distributions import get_sample

distributions = ["uniform", "harmonic", "snd_harmonic"]
functions = [hypercube_distance, torus_distance]
algorithms = [move_to_min, flip]


def experiment(iters=1000):
    costs = {}

    for d in distributions:
        print(d)
        costs[d] = {}

        for f in functions:
            print(f.__name__)
            costs[d][f.__name__] = Counter()
            for i in range(iters):
                if i % 50 == 0:
                    print(i)
                sample = get_sample(d)
                for alg in algorithms:
                    costs[d][f.__name__][alg.__name__] += alg(f, sample)

            for alg in algorithms:
                costs[d][f.__name__][alg.__name__] /= iters
                print(d, f.__name__, alg.__name__, costs[d][f.__name__][alg.__name__])

    with shelve.open("results") as db:
        db["costs"] = costs


if __name__ == "__main__":
    experiment()

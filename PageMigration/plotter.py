import shelve

from matplotlib import pyplot as plt

from algorithms import move_to_min, flip
from distances import hypercube_distance, torus_distance

distributions = ["uniform", "harmonic", "snd_harmonic"]
functions = [hypercube_distance, torus_distance]
algorithms = [move_to_min, flip]


def plot():
    with shelve.open("results", "r") as db:
        costs: dict = db["costs"]
    print(costs)
    keys = []
    values = []
    for d in distributions:
        for alg in algorithms:
            for f in functions:
                keys.append(f"{d[:3]}, {f.__name__[:5]}, {alg.__name__[:4]}")
                values.append(costs[d][f.__name__][alg.__name__])

    plt.rcParams.update({'font.size': 18})
    plt.figure(figsize=(22, 10))
    plt.barh(keys, values)
    plt.grid(visible=True)
    plt.ylabel("Configuration")
    plt.xlabel("Cost")
    plt.savefig("results.png")
    plt.close()


if __name__ == "__main__":
    plot()

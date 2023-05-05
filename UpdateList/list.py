from collections import Counter, defaultdict
from matplotlib import pyplot as plt

from probabilities import get_sample

counter = Counter()


def access(elem: int, l: list[int], self_organise):
    global counter
    counter[elem] += 1

    try:
        cost = l.index(elem) + 1
        l = self_organise(elem, l)

    except ValueError:
        cost = len(l)
        l.append(elem)

    return cost, l


def nothing(elem: int, l: list[int]):
    return l


def move_to_front(elem: int, l: list[int]):
    l.remove(elem)
    l.insert(0, elem)
    return l


def transpose(elem: int, l: list[int]):
    index = l.index(elem)
    if index > 0:
        l[index] = l[index - 1]
        l[index - 1] = elem
    return l


def count(elem: int, *args):
    return sorted(counter, key=counter.get, reverse=True)


def calc_avg_access_cost(n, distribution, self_organising_method):
    global counter
    counter = Counter()

    sample = get_sample(distribution=distribution, size=n)
    l = []
    cost_sum = 0
    for elem in sample:
        cost, l = access(elem, l, self_organising_method)
        cost_sum += cost
    return cost_sum / n


def experiment():
    no_experiments = 100
    n_values = [100, 500, 1000, 5000, 10000, 50000, 100000]
    distributions = ["uniform", "geometric", "harmonic", "snd_harmonic"]
    self_organising_methods = [nothing, move_to_front, transpose, count]

    for dist in distributions:
        avg_cost = defaultdict(dict)

        for method in self_organising_methods:
            for n in n_values:
                c = 0
                for i in range(no_experiments):
                    c += calc_avg_access_cost(n, dist, method)
                avg_cost[method][n] = c / no_experiments

        plt.figure()
        plt.title(dist)
        plt.xlabel("n")
        plt.ylabel("Access average cost")
        for method in self_organising_methods:
            avg_costs = avg_cost[method].items()
            avg_costs = sorted(avg_costs)
            x, y = zip(*avg_costs)
            plt.plot(x, y, label=method.__name__)
        plt.legend(loc='lower right')

        plt.savefig(f"{dist}")


if __name__ == '__main__':
    experiment()

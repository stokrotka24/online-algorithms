import shelve
from matplotlib import pyplot as plt
from experiment import algorithms, distributions, n_values


# def plot1():
#     for dist in distributions:
#         with shelve.open('result', 'r') as db:
#             avg_cost = db[dist]
#
#         for d in dividend:
#             plt.figure()
#             plt.title(f"{dist} k=n/{d}")
#             plt.xlabel("n")
#             plt.ylabel("Average cost of getting page")
#             for algorithm in algorithms:
#                 avg_costs = avg_cost[d][algorithm].items()
#                 avg_costs = sorted(avg_costs)
#                 x, y = zip(*avg_costs)
#                 plt.plot(x, y, label=algorithm)
#             plt.legend(loc='upper right')
#             plt.savefig(f"plots1/{dist}_k=n:{d}")
#             plt.close()
#
#
# def plot2():
#     for dist in distributions:
#         with shelve.open('result', 'r') as db:
#             avg_cost = db[dist]
#
#         for algorithm in algorithms:
#             plt.figure()
#             plt.title(f"{dist} {algorithm}")
#             plt.xlabel("n")
#             plt.ylabel("Average cost of getting page")
#             for d in dividend:
#                 avg_costs = avg_cost[d][algorithm].items()
#                 avg_costs = sorted(avg_costs)
#                 x, y = zip(*avg_costs)
#                 plt.plot(x, y, label=f"n/{d}")
#             plt.legend(loc='upper right')
#             plt.savefig(f"plots2/{dist} {algorithm}")
#             plt.close()

def plot():
    for dist in distributions:
        for n in n_values:
            with shelve.open(f'results/{dist}_n{n}', 'r') as db:
                avg_cost = db['results']
            plt.figure()
            plt.title(f"{dist} n={n}")
            plt.xlabel("k")
            plt.ylabel("Average cost of getting page")
            for algorithm in algorithms:
                avg_costs = avg_cost[algorithm].items()
                avg_costs = sorted(avg_costs)
                x, y = zip(*avg_costs)
                plt.plot(x, y, label=algorithm)
            plt.legend(loc='upper right')
            plt.savefig(f"plots/{dist}_n{n}")
            plt.close()


if __name__ == '__main__':
    # plot1()
    # plot2()
    plot()

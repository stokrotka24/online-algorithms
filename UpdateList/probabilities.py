import numpy as np


def harmonic_number(n):
    result = 1.00
    for i in range(2, n + 1):
        result += 1 / i
    return result


def snd_harmonic_number(n):
    result = 1.00
    for i in range(2, n + 1):
        result += 1 / i ** 2
    return result


def get_sample(distribution="uniform", size=100):
    possible_values = [*range(1, 101)]

    match distribution:
        case "uniform":
            return np.random.choice(a=possible_values, size=size, p=[1 / 100] * 100)
        case "geometric":
            geometric_probabilities = [1 / (2 ** i) for i in possible_values]
            geometric_probabilities[-1] = geometric_probabilities[-2]
            return np.random.choice(a=possible_values, size=size, p=geometric_probabilities)
        case "harmonic":
            h_100 = harmonic_number(100)
            return np.random.choice(a=possible_values, size=size, p=[1 / (i * h_100) for i in possible_values])
        case "snd_harmonic":
            h2_100 = snd_harmonic_number(100)
            return np.random.choice(a=possible_values, size=size, p=[1 / (i * i * h2_100) for i in possible_values])


# l = get_sample("harmonic", 1000)
# sum = sum(l)
# print(sum/1000)

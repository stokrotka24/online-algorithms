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


def get_sample(distribution, n, size):
    possible_values = [*range(1, n+1)]

    match distribution:
        case "uniform":
            return np.random.choice(a=possible_values, size=size, p=[1 / n] * n)
        case "geometric":
            geometric_probabilities = [1 / (2 ** i) for i in possible_values]
            geometric_probabilities[-1] = geometric_probabilities[-2]
            return np.random.choice(a=possible_values, size=size, p=geometric_probabilities)
        case "harmonic":
            h_n = harmonic_number(n)
            return np.random.choice(a=possible_values, size=size, p=[1 / (i * h_n) for i in possible_values])
        case "snd_harmonic":
            h2_n = snd_harmonic_number(n)
            return np.random.choice(a=possible_values, size=size, p=[1 / (i * i * h2_n) for i in possible_values])

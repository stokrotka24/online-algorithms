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


def get_sample(distribution, sample_size=1024, n=64):
    possible_values = [*range(1, n+1)]

    match distribution:
        case "uniform":
            probabilities = [1/n] * n
        case "harmonic":
            h_n = harmonic_number(n)
            probabilities = [1 / (i * h_n) for i in possible_values]
        case "snd_harmonic":
            h2_n = snd_harmonic_number(n)
            probabilities =[1 / (i * i * h2_n) for i in possible_values]

    return np.random.choice(a=possible_values, size=sample_size, p=probabilities)


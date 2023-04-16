import unittest

from distributions import harmonic_number, get_sample


class TestDistributions(unittest.TestCase):
    def test_harmonic_number(self):
        self.assertAlmostEquals(harmonic_number(1000), 7.485470860550345, places=10)

    def test_uniform(self):
        size = 10000
        n = 5000
        sample = get_sample(distribution="uniform", n=n, size=size)
        expected_value = n/2
        actual_value = sum(sample)/size
        print(f"\nUNIFORM: expected={expected_value} actual={actual_value}")
        self.assertTrue(abs(expected_value - actual_value) / expected_value < 0.03)

    def test_geometric(self):
        size = 10000
        n = 5000
        sample = get_sample(distribution="geometric", n=n, size=size)
        expected_value = 2
        actual_value = sum(sample) / size
        print(f"\nGEO: expected={expected_value} actual={actual_value}")
        self.assertTrue(abs(expected_value - actual_value) / expected_value < 0.03)

    def test_harmonic(self):
        size = 10000
        n = 5000
        sample = get_sample(distribution="harmonic", n=n, size=size)
        expected_value = n/harmonic_number(n)
        actual_value = sum(sample) / size
        print(f"\nGEO: expected={expected_value} actual={actual_value}")
        self.assertTrue(abs(expected_value - actual_value) / expected_value < 0.03)


import unittest

from cache.fifo import Fifo
from cache.fwf import Fwf
from cache.lfu import Lfu
from cache.lru import Lru
from cache.rand import Rand
from cache.rma import Rma


class TestCaches(unittest.TestCase):
    def test_fifo(self):
        c = Fifo(2)
        faults_num = 0

        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5])
        faults_num += c.get_page(3)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(1)
        self.assertEquals(c.cache, [3, 1])
        self.assertEquals(faults_num, 3)

    def test_fwf(self):
        c = Fwf(2)
        faults_num = 0

        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5])
        faults_num += c.get_page(3)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(1)
        self.assertEquals(c.cache, [1])
        self.assertEquals(faults_num, 3)

    def test_lru(self):
        c = Lru(2)
        faults_num = 0

        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5])
        faults_num += c.get_page(3)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [3, 5])
        faults_num += c.get_page(1)
        self.assertEquals(c.cache, [5, 1])
        self.assertEquals(faults_num, 3)

    def test_lfu(self):
        c = Lfu(2)
        faults_num = 0

        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5])
        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5])
        faults_num += c.get_page(3)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(1)
        self.assertEquals(c.cache, [5, 1])
        self.assertEquals(faults_num, 3)

    def test_rand(self):
        c = Rand(2)
        faults_num = 0

        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5])
        faults_num += c.get_page(3)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(1)
        self.assertTrue(c.cache == [5, 1] or c.cache == [3, 1])
        self.assertEquals(faults_num, 3)

    def test_rma(self):
        c = Rma(2)
        faults_num = 0

        faults_num += c.get_page(5)
        self.assertEquals(c.cache, [5])
        faults_num += c.get_page(3)
        self.assertEquals(c.cache, [5, 3])
        faults_num += c.get_page(1)
        self.assertTrue(c.cache == [5, 1] or c.cache == [3, 1])
        faults_num += c.get_page(2)
        self.assertEquals(c.cache, [1, 2])
        self.assertEquals(faults_num, 4)

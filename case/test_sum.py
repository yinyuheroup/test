import unittest

from tools.test_sum_1 import sum_1


class Test_data_sum(unittest.TestCase):
    def __init__(self,method, a, b, c):
        super().__init__(method)
        self.a = a
        self.b = b
        self.c = c

    def test_sum(self):
        self.assertEqual(self.c, sum_1(self.a, self.b))

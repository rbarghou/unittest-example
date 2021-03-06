import unittest
import scipy
from .utils import standard_deviation


class StandardDeviationTest(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            standard_deviation([1,2,3]),
            0.816496580927726
        )

    def test_against_scipy(self):
        for t in range(10):
            n = scipy.random.randint(10, 100)
            values = scipy.randn(n)
            self.assertTrue(
                abs(standard_deviation(values) - scipy.std(values)) < 10 ** -14
            )

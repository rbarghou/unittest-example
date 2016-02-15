# unittest-example
An example of how to use the unittest module in python.

Unit Testing
============

Unit testing is a technique for isolating "units" of code and sujecting them to
tests which help identify the unintended consiquences of changes or keep track
of errors in an actively developing codebase.

One of the benefits of isolating code units is that they can be tested
independently.

Unit Testing in Python
----------------------

Python's standard libraries come with the `unittest` package which can be used
to build whole unit test suites.  It provides a simple api for writing tests
along with the ability to run the whole suite and recursively discover tests.

Semantics, Syntax and Style
---------------------------

In our current example we have the following files.

```
└── src
    └── foo
        ├── __init__.py
        ├── tests.py
        └── utils.py
```

With the function in our utils method.
```python
# src/foo/utils.py
def standard_deviation(values):
    n = float(len(values))
    mean = sum(values) / n
    sum_squared_variances = sum([(x - mean) ** 2 for x in values])
    return (sum_squared_variances / n) ** .5
```
Suppose we wanted to ensure that this function worked as we imagined it.  To do
this we write a unittest in the `tests.py` module.

```python
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
```

This test file illustrates two different ways to write a test.

Please note that both tests make use of the `self.assertXxxx` pattern.
This pattern is available for a variety of different assertions and you should
make use of them.  They will give you useful error messages.

In the second test example, the `self.assertTrue` function gets called because
`scipy` and my naive implementation of `starndard_deviation` don't round in the
same ways.

Running Tests
-------------

Finally, to run all the tests in your src folder can execute this from the root
of the repository.

`ipython -m unittest discover src`

Note that if you are already in the `src` directory you can omit the last
argument.

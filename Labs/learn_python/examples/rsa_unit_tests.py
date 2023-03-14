"""
Example:    Example of how to test a class in python.

Date:       14/03/23

Think:      This file demonstrates the application of unit testing, consider 
            why testing is important for projects.
"""

import unittest 
from rsa import RSA

class TestConstructor(unittest.TestCase):
    
    def test_prime_inputs(self):
        pass

class TestIsPrime(unittest.TestCase):

    def test_is_negative(self):
        self.assertFalse(RSA.is_prime(-1))
        self.assertFalse(RSA.is_prime(-0))

    def test_is_even(self):
        self.assertFalse(RSA.is_prime(2))
        self.assertFalse(RSA.is_prime(34))

    def test_is_odd(self):
        self.assertFalse(RSA.is_prime(15))
        self.assertFalse(RSA.is_prime(99))

    def test_is_prime(self):
        self.assertTrue(RSA.is_prime(3))
        self.assertTrue(RSA.is_prime(23))


class TestKeyGenerators(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
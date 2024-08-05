import unittest
from factorials import factorial

class TestFactorial(unittest.TestCase):
    
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()

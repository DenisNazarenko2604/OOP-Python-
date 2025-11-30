import unittest
from main_Lesson_8 import *

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=15), 25)

    def test_mixed(self):
        self.assertEqual(adder(5, a=10), 15)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(adder(0, -5, a=x), 5)

    def test_wrong_datatype(self):
        self.assertEqual(adder("5", 10, "abc"), 15)

if __name__ == "__main__":
    unittest.main()

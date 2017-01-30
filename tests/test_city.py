import unittest
from united import importCity

class TestStringMethods(unittest.TestCase):



    def test_data_null(self):
        self.assertEqual(importCity("42.9098967654", "43.7653"),"jerusalem")

    def test_noneLat(self):
        self.assertEqual(importCity("",""), "")


if __name__ == '__main__':
    unittest.main()


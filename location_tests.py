import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    def test_repr1(self):
        loc = Location("OC", 27.2, -100.5)
        self.assertEqual(repr(loc),"Location('OC', 27.2, -100.5)")
    # Add more tests!
    def testcase1(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("OC", 27.2, -100.5)
        self.assertFalse(loc1==loc2)
    def testcase2(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1 == loc2)
    def testcase3(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 26.3, -120.7)
        self.assertFalse(loc1 == loc2)


if __name__ == "__main__":
        unittest.main()

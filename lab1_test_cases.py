import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter1(self):
        """add description here"""
        tlist = []
        self.assertEqual(max_list_iter(tlist),None)# used to check the empty list

    def test_max_list_iter2(self):
        """add description here"""
        tlist = [1,2,3,4,6,5]
        self.assertEqual(max_list_iter(tlist),6)# used to check the normal function of the code

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])# used to check the normal function of the code

    def test_reverse_rec1(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([11.3,2.3,3.2]),[3.2,2.3,11.3])# used to check the normal function of the code

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )# make sure function can handle even arrays

    def test_bin_search1(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4, 0, 7, tlist)

    def test_bin_search2(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 10
        self.assertEqual(bin_search(10, low, high, list_val), 10 )# checks to make sure it can detect the high slot

    def test_bin_search3(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 10
        self.assertEqual(bin_search(0, low, high, list_val), 0 )# checks to make sure it can detect the low

    def test_bin_search4(self):
        list_val =[0,1,2,3,4,7,8,9,10,11]
        low = 0
        high = 11
        self.assertEqual(bin_search(0, low, high, list_val), 0 )# make sure function can handle odd arrays

if __name__ == "__main__":
        unittest.main()

    

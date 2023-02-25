#test file
#tester job =)
'''
importing
'''
import unittest
from main import *

class Test2048(unittest.TestCase):

    def test_1(self): #test 1
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_2(self): #test 2
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_3(self): #test 3
        test_mas = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16]
        mas = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [1, 0, 0, 0],
               [0, 0, 3, 0]]
        self.assertEqual(get_empty_list(mas), test_mas)

    def test_4(self): #test 4
        test_mas = []
        mas = [[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]
        self.assertEqual(get_empty_list(mas), test_mas)

    def test_5(self): #test 5
        test_mas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
        self.assertEqual(get_empty_list(mas), test_mas)

    def test_6(self): #test 6
        self.assertEqual(get_index_from_number(16), (3, 0))

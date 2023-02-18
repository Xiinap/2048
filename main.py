# main file
'''
importing
'''
from logics import *  # from logics.py import all functions
import random

mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]  # massive 4x4

# reading massive
mas[2][0] = 2
mas[3][2] = 4

# using logics.py


while is_zero_in_mas(mas):
    '''
    getting random number in main
    '''
    input()
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num = empty.pop()
    row, col = get_index_from_number(random_num)
    mas = get_2_or_4(mas, row, col)
    print(f"WE FILL ELEMENT WITH NUMBER {random_num}")
    pretty_printer(mas)

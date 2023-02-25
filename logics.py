# logics file
"""
importing
"""
import random
'''
functions
'''
def pretty_printer(mas): #print massive in strokes
    print('-' * 8)
    for row in mas:
        print(*row)
    print('-' * 8)

def get_empty_list(mas):  # massive without elements
    empty = []
    for row in range(4):
        for col in range(4):
            if mas[row][col] == 0:
                num = get_number_from_index(row, col)
                empty.append(num)
    return empty

def get_number_from_index(row, col): #geting number from index
    return row * 4 + col + 1

def get_index_from_number(num): #geting index from number
    num -= 1
    row = num // 4
    col = num % 4

    return row, col

def get_2_or_4(mas, row, col): #geting two or four
    #for this function we cant create test because here is random n we cant test random =)
    if random.random() <= 0.8: #0.8 = 80 precent is two
        mas[row][col] = 2
    else:
        mas[row][col] = 4
    return mas

def is_zero_in_mas(mas): #True or False
    for row in mas:
        if 0 in row:
            return True
    return False

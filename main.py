# main file
'''
importing
'''
import pygame
from logics import *  # from logics.py import all functions
import sys
pygame.init()
from date_base import *
'''
drawing interface
'''
GAMER_DB = get_best()

def draw_top_gamers():
    font_best = pygame.font.SysFont('sixingkai', 20)
    text_best = font_best.render("Top players", 1, TEXT_COLOR)
    screen.blit(text_best, (275, 15))

    for index, gamer in enumerate(GAMER_DB):
        name = gamer[1]
        score = gamer[2]
        record = f"{index + 1}, {name} - {score}"
        text_gamer = font_best.render(record, 1, TEXT_COLOR)
        screen.blit(text_gamer, (275, 35 + 20 * index))

def draw_interface(score, delta=0):
    screen.fill(MARGIN_COLOR)
    pygame.draw.rect(screen, WHITE, TITLE_RECT)
    font = pygame.font.SysFont('sixingkai', 70)
    font_score = pygame.font.SysFont('sixingkai', 48)
    font_delta = pygame.font.SysFont('sixingkai', 24)
    text_score = font_score.render(f"Score: {score}", 1, TEXT_COLOR)
    screen.blit(text_score, (30, 30))

    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", 1, TEXT_COLOR)
        screen.blit(text_delta, (150, 65))

    draw_top_gamers()

    for row in range(BLOCKS):
        for col in range(BLOCKS):

            value = mas[row][col]

            if value < 8:
                text = font.render(f"{value}", 1, GRAY)
            else:
                text = font.render(f"{value}", 1, WHITE)

            if value >= 1024:
                font2 = pygame.font.SysFont('sixingkai', 59)
                text = font2.render(f"{value}", 1, WHITE)

            w = col * SIZE_BLOCK + (col + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))

            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))
'''
settings 
'''
#colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GRAY = [122, 118, 93]
MARGIN_COLOR = [187, 173, 162]
TEXT_COLOR = [255, 127, 0]

#library with colors for squares
COLORS = {
    0: [205, 193, 181],
    2: [240, 230, 221],
    4: [236, 223, 203],
    8: [241, 177, 123],
    16: [242, 152, 105],
    32: [242, 125, 105],
    64: [244, 96, 69],
    128: [235, 206, 118],
    256: [237, 203, 103],
    512: [236, 200, 89],
    1024: [232, 194, 88],
    2048: [176, 22, 219],
    4096: [29, 171, 55],
}

#sizes
BLOCKS = 4
SIZE_BLOCK = 100
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + SIZE_BLOCK
TITLE_RECT = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)

# massive 4x4
mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

score = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('4096 by Xiinap')
pygame.display.set_icon(pygame.image.load("icon.png"))

#reading massive
mas[random.randint(0, 3)][random.randint(0, 3)] = 2048
mas[random.randint(0, 3)][random.randint(0, 3)] = 2048
'''
mas[random.randint(0, 3)][random.randint(0, 3)] = 8
mas[random.randint(0, 3)][random.randint(0, 3)] = 16
mas[random.randint(0, 3)][random.randint(0, 3)] = 32
'''

draw_interface(score)
pygame.display.update()
'''
game while
'''
while is_zero_in_mas(mas):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)

            score += delta
            '''
            getting random number in main
            '''
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            row, col = get_index_from_number(random_num)
            mas = get_2_or_4(mas, row, col)
            #print(f"WE FILL ELEMENT WITH NUMBER {random_num}")
            #pretty_printer(mas)

            draw_interface(score, delta)
            pygame.display.update()

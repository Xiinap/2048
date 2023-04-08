import random

from logic import *
from database import cursor, get_best, insert_result
import pygame
import sys

GAMERS_DB = get_best()


def draw_top_gamers():
    font_top = pygame.font.SysFont('stxingkai', 20)
    text_best = font_top.render("Best results:", 1, TEXT_COLOR)
    screen.blit(text_best, (280, 15))

    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        record = f"{index + 1}. {name} - {score} "
        text_gamer = font_top.render(record, 1, TEXT_COLOR)
        screen.blit(text_gamer, (280, 35 + 20 * index))


def draw_intefce(score, delta=0):
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


    pretty_printer(mas)

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



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (122, 110, 93)
MARGIN_COLOR = (187, 173, 162)
TEXT_COLOR = (255, 127, 0)
COLORS = {
    0: (205, 193, 181),
    2: (240, 230, 221),
    4: (236, 223, 203),
    8: (241, 177, 123),
    16: (242, 152, 105),
    32: (242, 125, 99),
    64: (244, 96, 69),
    128: (235, 206, 118),
    256: (237, 203, 103),
    512: (236, 200, 89),
    1024: (232, 194, 88),
    2048: (176, 22, 219)

}

BLOCKS = 4
SIZE_BLOCK = 100
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + SIZE_BLOCK

def init_const():
    global score, mas
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num_1 = empty.pop()
    random_num_2 = empty.pop()
    x1, y1 = get_index_from_number(random_num_1)
    mas = insert_2_or_4(mas, x1, y1)
    x2, y2 = get_index_from_number(random_num_2)
    mas = insert_2_or_4(mas, x2, y2)
    score = 0


TITLE_RECT = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)

mas =None
score = None
init_const()
USERNAME = None

print(get_empty_list(mas))
pretty_printer(mas)

# for gamer in get_best():
#     print(gamer)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 by xiinap")

def draw_intro():
    img = pygame.image.load('2048.png')
    font = pygame.font.SysFont('stxingkai', 70)
    text_welcome = font.render("Welcome", 1, WHITE)
    name = 'Enter your name'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Enter your name':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, 1, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img, (150, 150)), (10, 10))
        screen.blit(text_welcome, (200, 50))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def draw_game_over():
    global  USERNAME, mas, score
    img = pygame.image.load('2048.png')
    font = pygame.font.SysFont('stxingkai', 48)
    text_game_over = font.render("GAME OVER!", 1, WHITE)
    text_score = font.render(f"You take: {score} points", 1, WHITE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = "New record!"
    else:
        text = f"Best result: {best_score}"
    text_record = font.render(text, 1, WHITE)
    insert_result(USERNAME, score)
    make_desicion = False
    while not make_desicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_desicion = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    USERNAME = None
                    make_desicion = True
                    init_const()
        screen.fill(BLACK)
        screen.blit(pygame.transform.scale(img, (150, 150)), (10, 10))
        screen.blit(text_game_over, (200, 50))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        pygame.display.update()
    screen.fill(BLACK)

def game_loop():

    global score, mas
    draw_intefce(score)
    pygame.display.update()
    while is_zero_in_mas(mas) or can_move(mas):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0

                if event.key == pygame.K_LEFT:
                    mas, delta = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta = move_rigth(mas)
                elif event.key == pygame.K_UP:
                    mas, delta = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta = move_down(mas)

                score += delta
                if is_zero_in_mas(mas):
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)
                    #print(f'Заполнен элемент под номером {random_num}')
                draw_intefce(score, delta)
                pygame.display.update()

while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    draw_game_over()

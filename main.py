import random
from time import sleep

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
a = pygame.image.load('snake.png')
pygame.display.set_icon(a)
pygame.display.set_caption("Python Snake")
x = 300
y = 300
eyeoffsetx=0
eyeoffsety=0
eyeoffsetx2=0
eyeoffsety2=0
speed = 1
width = 30
height = 30
direction = "R"
odl = ""
go = True
nextDirection = "R"
oldDirection = "R"
score = 0

snake_pos = [120, 120]
snake_body = [[120, 120], [120 - 30, 120], [120 - (2 * 30), 120], [120 - (3 * 30), 120]]
food_pos = [random.randrange(1, (600 // 30)) * 30, random.randrange(1, (600 // 30)) * 30]
food_spawn = True


def redraw():
    c = 0
    while c < screen.get_height():
        a = 0
        while a < screen.get_width() / 2:
            pygame.draw.rect(screen, (0, 200, 20), (0 + a * 2, 0 + c, 30, 30))
            a += 30
        a = 0
        while a < screen.get_width() / 2:
            pygame.draw.rect(screen, (0, 200, 20), (30 + a * 2, 30 + c, 30, 30))
            a += 30
        b = 0
        while b < screen.get_width() / 2:
            pygame.draw.rect(screen, (0, 220, 0), (30 + b * 2, 0 + c, 30, 30))
            b += 30
        b = 0
        while b < screen.get_width() / 2:
            pygame.draw.rect(screen, (0, 220, 0), (0 + b * 2, 30 + c, 30, 30))
            b += 30
        c += 60


def game_over():

    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Game Over', True, (180,0,0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (600 / 2, (600 / 2)-100)
    #screen.fill((0, 0, 0))
    screen.blit(game_over_surface, game_over_rect)
    show_score()
    pygame.display.flip()
    sleep(3)


def show_score():
    font = pygame.font.SysFont('consolas', 20)
    text = font.render('Score: ' + str(score), False, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (50, 18)
    screen.blit(text, textRect)


i = 0
while i < 20:
    snake_body.insert(0, list(snake_pos))
    i += 1

while go:
    snake_body.insert(0, list(snake_pos))

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
        if score % 3 == 0:
            speed += 1
    else:
        snake_body.pop()
    if not food_spawn:
        food_pos = [random.randrange(1, (600 // 30)) * 30, random.randrange(1, (600 // 30)) * 30]
    food_spawn = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_w] or pressed[pygame.K_UP]) and direction != "D":
        nextDirection = "U"
    elif (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]) and direction != "L":
        nextDirection = "R"
    elif (pressed[pygame.K_s] or pressed[pygame.K_DOWN]) and direction != "U":
        nextDirection = "D"
    elif (pressed[pygame.K_a] or pressed[pygame.K_LEFT]) and direction != "R":
        nextDirection = "L"

    if snake_pos[0] % 30 == 0 and snake_pos[1] % 30 == 0:
        oldDirection = direction
        direction = nextDirection

    if direction == "R":
        snake_pos[0] += speed
        eyeoffsetx=15
        eyeoffsety=3
        eyeoffsetx2 = 15
        eyeoffsety2 = 27
    elif direction == "D":
        snake_pos[1] += speed
        eyeoffsetx = 27
        eyeoffsety = 15
        eyeoffsetx2 = 3
        eyeoffsety2 = 15
    elif direction == "L":
        snake_pos[0] -= speed
        eyeoffsetx = 15
        eyeoffsety = 3
        eyeoffsetx2 = 15
        eyeoffsety2 = 27
    elif direction == "U":
        snake_pos[1] -= speed
        eyeoffsetx = 3
        eyeoffsety = 15
        eyeoffsetx2 = 27
        eyeoffsety2 = 15
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 30, 30))

    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(pos[0], pos[1], 30, 30))

    pygame.draw.circle(screen, (255, 255, 255), (snake_pos[0]+eyeoffsetx, snake_pos[1]+eyeoffsety), 6, 6)
    pygame.draw.circle(screen, (255, 255, 255), (snake_pos[0]+eyeoffsetx2, snake_pos[1]+eyeoffsety2), 6, 6)

    pygame.draw.circle(screen, (0, 0, 0), (snake_pos[0] + eyeoffsetx+1, snake_pos[1] + eyeoffsety+1), 2, 2)
    pygame.draw.circle(screen, (0, 0, 0), (snake_pos[0] + eyeoffsetx2+1, snake_pos[1] + eyeoffsety2+1), 2, 2)
    if snake_pos[0] <= -5 or snake_pos[0] >= 575 or snake_pos[1] <= -5 or snake_pos[1] >= 575:
        game_over()
        break
    show_score()
    pygame.display.update()
    clock.tick(60)
    redraw()


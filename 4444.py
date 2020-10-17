# coding=utf-8
import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

# здесь вводим переменные цветов, чтобы цвет следующего щарика был случайным
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# пишем функцию создания случайного шарика
class Ball:
    vx = 0
    vy = 0
    x = 0
    y = 0
    r = 0
    color = BLACK
    def new(self):
        a = randint(0, 360)
        self.vx = 5 * np.cos(2 * np.pi * a / 360)
        self.vy = 5 * np.sin(2 * np.pi * a / 360)
        self.x = randint(50, 1150)
        self.y = randint(50, 850)
        self.r = randint(30, 50)
        self.color = COLORS[randint(0, 5)]
    pass


def click(event):
    print(x, y, r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
k = 0
j = 0
balls_list = (Ball())
while not finished:
    for i in range(FPS*3):
        clock.tick(FPS)
        for i in range(j):
            x = balls_list[i].x
            y = balls_list[i].y
            vx = balls_list[i].vx
            vy = balls_list[i].vy
            r = balls_list[i].r
            color = balls_list[i].color
            b = randint(0, 90)
            if (0 > y - r) | (y + r > 900):
                vy = -vy / (vy**2)**0.5 * 5 * np.sin(2*np.pi/360 * b)
                vx = vx / (vx**2)**0.5 * 5 * np.cos(2*np.pi/360 * b)
            if (0 > x - r) | (x + r > 1200):
                vy = vy / (vy ** 2) ** 0.5 * 5 * np.sin(2 * np.pi / 360 * b)
                vx = -vx / (vx ** 2) ** 0.5 * 5 * np.cos(2 * np.pi / 360 * b)
            x = x + vx
            y = y + vy
            circle(screen, color, (int(x), int(y)), r)
            balls_list[i].x = x
            balls_list[i].y = y
            balls_list[i].vx = vx
            balls_list[i].vy = vy
            balls_list[i].r = r
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')
                click(event)
                for i in range (j):
                    x = balls_list[i].x
                    y = balls_list[i].y
                    r = balls_list[i].r
                    if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 < r**2:
                        k += 1
    j = randint(2, 5)
    balls_list = list()
    for i in range(0, j):
        ball = Ball()
        ball.new()
        balls_list.append(ball)
    pygame.display.update()
    screen.fill(BLACK)

print(k)
pygame.quit()

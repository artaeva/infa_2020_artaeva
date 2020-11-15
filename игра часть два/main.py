# coding=utf-8
import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))

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
        self.y = randint(50, 650)
        self.r = randint(30, 50)
        self.color = COLORS[randint(0, 5)]
    pass


class Star:
    v = 0 # скорость звезды
    a = 0 # горизонтально или вертикально будет двигаться звезда?
    x = 0
    y = 0
    r = 0
    color = BLACK
    def new (self):
        self.v = randint(3, 10)
        self.a = randint(0, 1)
        self.x = randint(100, 1100)
        self.y = randint(60, 640)
        self.r = randint(30, 60)
        self.color = COLORS[randint(0, 5)]
    def draw (self):
        polygon(screen, self.color, ((self.x, self.y - self.r), (self.x+10, self.y-14), (self.x+int(r*0.95), self.y-int(r*0.3)), (self.x+18, self.y+6), (self.x+int(r*0.58), self.y+int(r*0.8)), (self.x, self.y+20), (self.x-int(r*0.58), self.y+int(r*0.8)), (self.x-18, self.y+6), (self.x-int(r*0.95), self.y-int(r*0.3)), (self.x-10, self.y-14)))


def click(event):
    print(x, y, r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
k = 0
print('введите имя игрока одним словом')
name = str(input())
j = randint(2, 5)
balls_list = list()
for i in range(0, j):
    ball = Ball()
    ball.new()
    balls_list.append(ball)
l = randint(1, 4)
stars_list = list()
for i in range(0, l):
    star = Star()
    star.new()
    stars_list.append(star)
while not finished:
    for m in range(FPS):
        clock.tick(FPS)
        for i in range(j):
            x = balls_list[i].x
            y = balls_list[i].y
            vx = balls_list[i].vx
            vy = balls_list[i].vy
            r = balls_list[i].r
            color = balls_list[i].color
            b = randint(1, 89)
            if (0 > y - r) | (y + r > 900):
                 vy = -vy / (vy**2)**0.5 * 5 * np.sin(2*np.pi/360 * b)
                 vx = vx / (vx**2)**0.5 * 5 * np.cos(2*np.pi/360 * b)
            if (0 > x - r) | (x + r > 1200):
                vy = vy / (vy ** 2) ** 0.5 * 5 * np.sin(2 * np.pi / 360 * b)
                vx = -vx / (vx ** 2) ** 0.5 * 5 * np.cos(2 * np.pi / 360 * b)
            x = int(x + vx)
            y = int(y + vy)
            circle(screen, color, (int(x), int(y)), r)
            balls_list[i].x = x
            balls_list[i].y = y
            balls_list[i].vx = vx
            balls_list[i].vy = vy
            balls_list[i].r = r
        for i in range(l):
             x = stars_list[i].x
             y = stars_list[i].y
             v = stars_list[i].v
             a = stars_list[i].a
             r = stars_list[i].r
             color = stars_list[i].color
             x = int(x + a * v * (-1)**(int(m/10)))
             y = int(y + (1-a) * v * (-1)**(int(m/6)))
             stars_list[i].draw()
             stars_list[i].x = x
             stars_list[i].y = y
             stars_list[i].v = v
             stars_list[i].r = r
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')
                click(event)
                for i in range(j):
                    x = balls_list[i].x
                    y = balls_list[i].y
                    r = balls_list[i].r
                    if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 < r**2:
                        k += 1
                for i in range (l):
                     x = stars_list[i].x
                     y = stars_list[i].y
                     r = stars_list[i].r
                     if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 < (r/2+10)**2:
                         k += 2
    j = randint(2, 5)
    balls_list = list()
    for i in range(0, j):
         ball = Ball()
         ball.new()
         balls_list.append(ball)
    l = randint(1, 4)
    stars_list = list()
    for i in range(0, l):
         star = Star()
         star.new()
         stars_list.append(star)
    pygame.display.update()
    screen.fill(BLACK)
print(k)
pygame.quit()
inp = open('1.txt', 'r')
a = inp.readlines()
b = list()
for i in range(len(a)):
    b.extend(a[i].split())

c = list()
for i in range(int(len(b)/2)):
    c.append(int(b[2*i+1]))
i = 0
s = 0
while s == 0 and i < int(len(c)):
    if c[i] > k:
        i+=1
    else:
        s = 1
b.insert(2*i, name)
b.insert(2*i+1, str(k))
inp.close()
out = open('1.txt', 'w')
for i in range(len(a)+1):
    out.write(b[2*i] + ' ')
    out.write(b[2*i+1] + '\n')
out.close()
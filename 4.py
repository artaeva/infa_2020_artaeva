# coding=utf-8
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))
def ground(surface, color_sky, color_ground):
    '''
    Функция рисует фон - небо и землю
    surface - объект pygame.Surface
    color_sky - цвет неба
    color_ground - цвет земли
    '''
    rect(surface, color_ground, (0, 250, 400, 350), 0)
    rect(surface, color_sky, (0, 0, 400, 250), 0)
    pass

def solntse(surface, (x, y), radius):
    '''
    Функция рисует солнце
    surface - объект pygame.Surface
    x, y - координаты центра солнца
    radius - радиус солнца
    '''
    circle(surface, (255, 255, 255), (x, y), radius, 0)
    pass

def oblako(surface, x, y, width, height):
    '''
    Функция рисует облако
    surface -  объект pygame.Surface
    x, y - координаты левого верхнего угла прямоугольника, в который вписан эллипс облака
    width - ширина облака
    height - высота облака
    '''
    for i in range(11, 0, -1):
        f = 70 - 7 * i
        ellipse(surface, (20 + 10 * i, 20 + 10 * i, 20 + 10 * i), (x + f, y + 0.5 * f, width - 2 * f, height - f))
        pass


def svet(surface, x, y, width, height):
    '''
    Функция рисует свет, падающий из тарелки
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла прямоугольника, в который вписан эллипс тарелки, из которой падает свет
    width - ширина тарелки, из которой падает свет, поделённая на 140
    height - высота тарелки, из которой падает свет, поделённая на 70
    '''
    polygon(surface, (101, 150, 132), [(x + 5 + width * 5, y + 140 + height * 160), (x + 5 + width * 145, y + 140 + height * 160),
                                            (x + 5 + width * 117, y + 140 + height * 110), (x + 5 + width * 33, y + 140 + height * 110)], 0)
    polygon(surface, (100, 100, 239), [(x + 5 + width * 33, y + 140 + height * 110), (x + 5 + width * 117, y + 140 + height * 110),
                                            (x + 5 + width * 75, y + 140 + height * 35)], 0)
    pass


def tarelka(surface, x, y, width, height):
    '''
    Функция рисует летающую тарелку
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла прямоугольника, в который вписан эллипс тарелки
    width - ширина тарелки, поделённая на 140
    height - высота тарелки, поделённая на 70
    '''
    svet(surface, x, y, width, height)
    ellipse(screen, (50, 50, 50), (x + 5, y + 140, width * 140, height * 70))
    ellipse(screen, (100, 100, 100), (x + 5 + width * 25, y + 140, width * 90, height * 45))
    ellipse(screen, (200, 200, 200), (x + 5 + width * 13, y + 140 + height * 36, width * 20, height * 10))
    ellipse(screen, (200, 200, 200), (x + 5 + width * 28, y + 140 + height * 48, width * 20, height * 10))
    ellipse(screen, (200, 200, 200), (x + 5 + width * 50, y + 140 + height * 54, width * 20, height * 10))
    ellipse(screen, (200, 200, 200), (x + 5 + width * 107, y + 140 + height * 36, width * 20, height * 10))
    ellipse(screen, (200, 200, 200), (x + 5 + width * 92, y + 140 + height * 48, width * 20, height * 10))
    ellipse(screen, (200, 200, 200), (x + 5 + width * 70, y + 140 + height * 54, width * 20, height * 10))

def chelic(surface, x, y, x1, z):
    '''
    Функция рисует инопланетянина
    surface - объект pygame.Surface
    x, y - координаты конца верхнего левого уха инопланетянина
    x1 - ширина туловища инопланетянина, делённая на 35
    z - переменная, отвечающая за ориентацию (если 1, то инопланетянин смотрит вправо, если 0, то влево)
    '''
    scr1 = pygame.Surface((87, 163))
    ellipse(scr1, (101, 200, 132), (17, 65, 35, 70))
    ellipse(scr1, (101, 200, 132), (50, 75, 10, 10))
    ellipse(scr1, (101, 200, 132), (55, 80, 10, 7))
    ellipse(scr1, (101, 200, 132), (62, 85, 14, 10))

    ellipse(scr1, (101, 200, 132), (10, 75, 10, 10))
    ellipse(scr1, (101, 200, 132), (5, 80, 10, 10))
    ellipse(scr1, (101, 200, 132), (0, 90, 5, 8))

    ellipse(scr1, (101, 200, 132), (45, 120, 10, 20))
    ellipse(scr1, (101, 200, 132), (47, 137, 10, 20))
    ellipse(scr1, (101, 200, 132), (52, 153, 10, 10))

    ellipse(scr1, (101, 200, 132), (10, 115, 10, 20))
    ellipse(scr1, (101, 200, 132), (7, 132, 10, 21))
    ellipse(scr1, (101, 200, 132), (0, 145, 10, 10))

    ellipse(scr1, (101, 200, 132), (20, 28, 40, 40))

    ellipse(scr1, (101, 200, 132), (15, 25, 10, 10))
    ellipse(scr1, (101, 200, 132), (10, 10, 10, 15))
    ellipse(scr1, (101, 200, 132), (5, 0, 10, 10))

    ellipse(scr1, (101, 200, 132), (55, 25, 10, 10))
    ellipse(scr1, (101, 200, 132), (60, 10, 10, 15))
    ellipse(scr1, (101, 200, 132), (73, 5, 10, 10))

    ellipse(scr1, (0, 0, 0), (27, 37, 10, 10))
    ellipse(scr1, (225, 225, 225), (32, 42, 2, 2))
    ellipse(scr1, (0, 0, 0), (45, 40, 8, 8))
    ellipse(scr1, (225, 225, 225), (49, 44, 2, 2))

    ellipse(scr1, (255, 100, 100), (67, 67, 20, 20))
    ellipse(scr1, (101, 200, 132), (76, 62, 2, 5))

    scr1 = pygame.transform.scale(scr1, (int(x1*100), int(x1*100*163.0/87)))
    scr1 = pygame.transform.flip(scr1, z, 0)
    surface.blit(scr1, (x, y))

ground(screen, (0, 0, 139), (1, 50, 32))
solntse(screen, (260, 70), 50)

oblako(screen, 15, 90, 300, 80)
oblako(screen, 300, 150, 200, 60)
oblako(screen, 240, 40, 100, 15)
oblako(screen, -100, 20, 300, 80)
oblako(screen, 44, 100, 200, 30)

tarelka(screen, 0, 0, 1, 1)
tarelka(screen, 300, 27, 0.75, 0.75)
tarelka(screen, 200, 54, 0.5, 0.5)

chelic(screen, 282, 400, 1, 0)
chelic(screen, 132, 420, 0.6, 1)
chelic(screen, 102, 290, 0.5, 1)
chelic(screen, 32, 350, 0.4, 1)
chelic(screen, 172, 340, 0.3, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
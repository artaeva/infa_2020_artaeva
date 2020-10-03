import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
 #цвет экрана
polygon(screen, (235, 255, 205), [(0,0), (500, 0), (500, 500), (0, 500)], 0)
#лицо смайлика
circle(screen, (255, 255, 0), (250, 250), 150, 0)
circle(screen, (0, 0, 0), (250, 250), 150, 1)
#глаза смайлика
circle(screen, (255, 0, 0), (190, 200), 40, 0)
circle(screen, (0, 0, 0), (190, 200), 40, 1)
circle(screen, (255, 0, 0), (310, 200), 30, 0)
circle(screen, (0, 0, 0), (310, 200), 30, 1)
circle(screen, (0, 0, 0), (190, 200), 15, 0)
circle(screen, (0, 0, 0), (310, 200), 15, 0)
#брови и рот
polygon(screen, (0, 0, 0), [(190, 300), (310, 300), (310, 320), (190, 320), (190, 300)], 0)
polygon(screen, (0, 0, 0), [(240, 178), (110, 128), (115, 118), (245, 168), (240, 178)], 0)
polygon(screen, (0, 0, 0), [(260, 173), (380, 135), (385, 143), (265, 183), (260, 173)], 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

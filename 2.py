import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

polygon(screen, (0, 255, 255), [(0,0), (500, 0), (500, 370), (0, 370)], 0)
polygon(screen, (220, 220, 220), [(0, 370), (500, 370), (500, 700), (0, 700)], 0)
line(screen, (0, 0, 0), (0, 370), (500, 370), 1)

#напишем функию, которая будет возвращать поверхность, на которой нарисован медведь
def bear():
    scrprorub = pygame.Surface((300, 600))
    ellipse(scrprorub, (75, 75, 75), (0, 0, 200, 80), 0)
    ellipse(scrprorub, (0, 0, 0), (0, 0, 200, 80), 1)
    ellipse(scrprorub, (25, 75, 70), (25, 25, 150, 55), 0)
    ellipse(scrprorub, (0, 0, 0), (25, 25, 150, 55), 1)

    scrbear = pygame.Surface((800, 800))
    ellipse(scrbear, (220, 220, 220), (80, 200, 200, 300), 0)
    ellipse(scrbear, (0, 0, 0), (80, 200, 200, 300), 1)
    ellipse(scrbear, (220, 220, 220), (180, 400, 150, 100), 0)
    ellipse(scrbear, (0, 0, 0), (180, 400, 150, 100), 1)
    ellipse(scrbear, (220, 220, 220), (280, 484, 112, 33), 0)
    ellipse(scrbear, (0, 0, 0), (280, 484, 112, 33), 1)
    ellipse(scrbear, (220, 220, 220), (180, 170, 100, 60), 0)
    ellipse(scrbear, (0, 0, 0), (180, 170, 100, 60), 1)
    ellipse(scrbear, (220, 220, 220), (180, 170, 16, 15), 0)
    ellipse(scrbear, (0, 0, 0), (180, 170, 16, 15), 1)
    circle(scrbear, (0, 0, 0), (217, 193), 5, 0)
    circle(scrbear, (0, 0, 0), (280, 200), 5, 0)
    arc(scrbear, (0, 0, 0), (180, 190, 100, 30), 3*3.14/2, 2*3.14, 2)
    line(scrbear, (0, 0, 0), (250, 400), (280, 300), 5)
    line(scrbear, (0, 0, 0), (280, 300), (350, 180), 5)
    arc(scrbear, (0, 0, 0), (348, 176, 20, 20), 2*3.14/3, 3.14, 5)
    line(scrbear, (0, 0, 0), (352, 180), (450, 120), 5)
    scrbear.blit(scrprorub, (370, 410))
    line(scrbear, (0, 0, 0), (450, 120), (450, 450), 2)
    ellipse(scrbear, (220, 220, 220), (255, 300, 66, 33), 0)
    ellipse(scrbear, (0, 0, 0), (255, 300, 66, 33), 1)

#напишем поверхность с рыбой
    scrfish = pygame.Surface((400, 400))
    polygon(scrfish, (255, 0, 0), [[260, 330], [240, 350], [280, 350]])
    polygon(scrfish, (0, 0, 0), [[260, 330], [240, 350], [280, 350]],1)
    polygon(scrfish, (255, 0, 0), [[250, 345], [250, 363], [235, 360]])
    polygon(scrfish, (0, 0, 0), [[250, 345], [250, 363], [235, 360]],1)
    polygon(scrfish, (255, 0, 0), [[267, 345], [267, 363], [282, 368]])
    polygon(scrfish, (0, 0, 0), [[267, 345], [267, 363], [282, 368]],1)
    polygon(scrfish, (150, 200, 150), [[235, 348], [210, 358], [210, 338]])
    polygon(scrfish, (0, 0, 0), [[235, 348], [210, 358], [210, 338]],1)
    ellipse(scrfish, (150, 200, 150), (230, 338, 60, 20))
    ellipse(scrfish, (0, 0, 0), (230, 338, 60, 20), 1)
    ellipse(scrfish, (0, 0, 0), (276, 343, 10, 10))
    ellipse(scrfish, (255, 255, 255), (280, 345, 5, 5))

#на поверхность с медведем добавим семь рыб
    scrfish = pygame.transform.rotate(scrfish, 15)
    scrbear.blit(scrfish, (100, 160))
    scrfish = pygame.transform.rotate(scrfish, -5)
    scrfish = pygame.transform.flip(scrfish, 1, 0)
    scrbear.blit(scrfish, (350, 140))
    scrfish = pygame.transform.rotate(scrfish,10)
    scrbear.blit(scrfish, (240, 60))
    scrfish = pygame.transform.flip(scrfish, 1, 0)
    scrfish = pygame.transform.rotate(scrfish, -10)
    scrbear.blit(scrfish, (160, 0))
    scrfish = pygame.transform.scale(scrfish, (380, 380))
    scrfish = pygame.transform.flip(scrfish, 0, 1)
    scrfish = pygame.transform.rotate(scrfish, -20)
    scrbear.blit(scrfish, (130, 230))
    scrfish = pygame.transform.flip(scrfish, 1, 1)
    scrbear.blit(scrfish, (270, 70))
    scrfish = pygame.transform.flip(scrfish, 0, 1)
    scrbear.blit(scrfish, (310, 230))
    return scrbear

#нарисуем поверхность с крестиком
scr4 = pygame.Surface((900, 900))
circle(scr4, (210, 240, 215), (250, 250), 150, 30)
line(scr4, (210, 240, 215), (100, 240), (400, 260), 25)
line(scr4, (210, 240, 215), (240, 390), (260, 110), 25)
circle(scr4, (255, 255, 200), (120, 240), 15)
circle(scr4, (255, 255, 200), (390, 260), 15)
circle(scr4, (255, 255, 200), (240, 390), 15)
circle(scr4, (255, 255, 200), (260, 110), 15)
circle(scr4, (255, 255, 200), (250, 250), 15)

screen.blit(scr4, (70, -100))

scr2 = pygame.transform.scale(bear(), (600, 600))
screen.blit(scr2, (20, 200))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

import pygame
from pygame.draw import *

pygame.init()
print('введите радиус злого смайлика')
R = int(input())

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))

circle(screen, (255, 255, 0),(200, 200), R)
circle(screen, (255, 0, 0),(200 - R//2, 200 - R//2), R//5)
circle(screen, (0, 0, 0),(200 - R//2, 200 - R//2), R//10)
circle(screen, (255, 0, 0),(200 + R//2, 200 - R//2), R//6)
circle(screen, (0, 0, 0),(200 + R//2, 200 - R//2), R//12)
polygon(screen, (0, 0, 0), [(200 + R,200 - R), (215 + R,215 - R), (150 + R//2, 200 - R//2), (145 + R//2, 195 - R//2)])
polygon(screen, (0, 0, 0), [(200 - R,200 - R), (185 - R,215 - R), (250 - R//2, 200 - R//2), (255 - R//2, 195 - R//2)])
rect(screen, (0, 0, 0), (200 - R//2, 200 + R//2, R, R//12))                                
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

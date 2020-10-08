import pygame
import numpy as np
import pygame.draw as pgd

pygame.init()
screen = pygame.display.set_mode((800, 600))

COLOR = {
'Orange'      : (255, 178,   0),
'Human'       : (255, 218, 185),
'Pink'        : (255,  20, 147),
'Blue'        : (  0,   0, 139),
'Black'       : (  0,   0,   0),
'SkyBlue'     : (135, 206, 235),
'ForestGreen' : ( 34, 139,  34),
'Red'         : (255,   0,   0),
'Maroon'      : (128,   0,   0),
'White'       : (255, 255, 255)}

R_of_head = 30 # радиус головы человечка
human_height = 150 # высота туловища человечка
human_y = 250 # координата (y) макушки человечка
FPS = 30
k = 160 # Константа, отвечающая за расстояние между человечками по оси X.


# Функция, рисуюшая равнобедренный трегольник с координатами  середины основания (x, y), высотой h, цветом color, основанием 2a и углом между основанием и горизонталью f.
def draw_triangle(color, x, y, a, h, f):
    pgd.polygon(screen, color, [(x - a*np.cos(f), y + a*np.sin(f)), (x + a*np.cos(f), y - a*np.sin(f)), (x + h*np.sin(f), y + h*np.cos(f))])    


# Функция, рисующая букет цветов.
def draw_flavour(x, y, a, h, f, colors = (COLOR['Orange'], COLOR['Red'], COLOR['Maroon'], COLOR['White'])):
    draw_triangle(colors[0], x, y, a, h, f) 
    pgd.circle(screen, colors[1], (int(round(x + a*np.cos(f)/2)), int(round(y - a*np.sin(f)/2))), a//2) 
    pgd.circle(screen, colors[2], (int(round(x - a*np.cos(f)/2)), int(round(y - a*np.sin(f)/2))), a//2)
    pgd.circle(screen, colors[3], (int(round(x - 0.6*a*np.sin(f))), int(round(y - 0.6*a*np.cos(f)))), a//2)

    
#Функция, рисующая шарик - сердечко.
def draw_heart(x, y, a, h, f, color = COLOR['Red']):
    draw_triangle(color, x, y, a, h, f)
    pgd.circle(screen, color, (int(round(x + a*np.cos(f)/2)), int(round(y - a*np.sin(f)/2))), a//2) 
    pgd.circle(screen, color, (int(round(x - a*np.cos(f)/2)), int(round(y - a*np.sin(f)/2))), a//2)

screen.fill(COLOR['SkyBlue'])
pgd.rect(screen, COLOR['ForestGreen'], (0, 300, 800, 300))
draw_flavour(400, 100, 40, 80, np.pi/20 )
draw_flavour(750, 320, 20, 40, -np.pi/15)
draw_heart(50, 200, 30, 60, 0)

pgd.aalines(screen, COLOR['Black'], False, [[400 + 80*np.sin(np.pi/20), 100 + 80*np.cos(np.pi/20)],
                                   [k*3 - (0.5)*11*R_of_head/2,human_y + 3*R_of_head]])
pgd.aalines(screen, COLOR['Black'], False, [[50 + 60*np.sin(0), 200 + 60*np.cos(0)],
                                   [k*1 - 3*R_of_head*0.9, human_y + 5*R_of_head*0.9]])
pgd.aalines(screen, COLOR['Black'], False, [[750 + 40*np.sin(-np.pi/15), 320 + 40*np.cos(-np.pi/15)],
                                   [k*4 + 3*R_of_head*0.9, human_y + 5*R_of_head*0.9]])

# Рисуем девочек.
for i in range(2,4):
    pgd.aalines(screen, COLOR['Black'], False, [[k*i + (i - 2.5)*2*R_of_head/2, human_y + 2.5*R_of_head],
                                   [k*i + (i - 2.5)*6*R_of_head*0.9, human_y + 5*R_of_head*0.9]])
    pgd.aalines(screen, COLOR['Black'], False, [[k*i - (i - 2.5)*2*R_of_head/2, human_y + 2.5*R_of_head],
                                   [k*i - (i - 2.5)*10*R_of_head/4, human_y + 4*R_of_head],
                                   [k*i - (i - 2.5)*11*R_of_head/2, human_y + 3*R_of_head]]) 
    for p in range (-1, 3, 2):
        pgd.aalines(screen, COLOR['Black'], False, [[k*i + p* R_of_head/2, human_y + 3.3*R_of_head],
                                       [k*i + p*5*R_of_head/8, human_y + 7*R_of_head/2 + human_height],
                                       [k*i + p*R_of_head, human_y + 7*R_of_head/2 + human_height]])
    draw_triangle(COLOR['Pink'], k*i, human_y + 3*R_of_head/2 + human_height, 2*R_of_head, human_height, np.pi/1)
    pgd.circle(screen, COLOR['Human'], (k*i, human_y + R_of_head), R_of_head)
    
# Рисуем мальчиков. 
for i in range(1, 5, 3):
    for p in range (-1, 3, 2):
        pgd.aalines(screen, COLOR['Black'], False, [[k*i + p*R_of_head/2, human_y + 2.5*R_of_head],
                                        [k*i + p*3*R_of_head*0.9, human_y + 5*R_of_head*0.9]])
        pgd.aalines(screen, COLOR['Black'], False, [[k*i + p* R_of_head/2, human_y + 3.3*R_of_head],
                                       [k*i + p*5*R_of_head/8,  human_y + 7*R_of_head/2 +human_height],
                                       [k*i + p*R_of_head,  human_y + 7*R_of_head/2 + human_height]])
    pgd.ellipse(screen, COLOR['Blue'], (k*i - R_of_head, human_y + 3*R_of_head/2, 2*R_of_head, human_height)) 
    pgd.circle(screen, COLOR['Human'], (k*i, human_y + R_of_head), R_of_head)
       
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


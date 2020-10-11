import pygame
import numpy as np
import pygame.draw as pgd

X, Y = (800, 600) #размеры окна
FPS = 30

COLOR = {                       #Словарь цветов
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

HUMAN = {      #Словарь геометрических параметров человечка
'Head'   :  30,
'Height' : 150,
'Hand'   :  70,
'y_hand' :  10,
'y_leg'  : 130,
'foot'   :  25,
'Dist'   : 160}

pygame.init()
screen = pygame.display.set_mode((X, Y))


def draw_triangle(color, x, y, a, h, f):
    '''
    Рисует равнобедренный треугольник по заданным высоте и основанию, с заданием угла поворота
    ----------------------------------------------------------
    color - цвет
    x - горизонтальная координата центра основания треугольника
    y - вертикальная координата центра основания треугольника
    a - основание
    h - высота
    f - угол поворота фигуры
    '''
    pgd.polygon(screen, color, [(x - a*np.cos(f), y + a*np.sin(f)), (x + a*np.cos(f), y - a*np.sin(f)), (x + h*np.sin(f), y + h*np.cos(f))])    


def draw_flavour(x, y, a, h, f, xline, yline, colors = (COLOR['Orange'], COLOR['Red'  ], COLOR['Maroon'], 
                                                                         COLOR['White'], COLOR['Black' ])):
    '''
    Рисует шарик-букет с заданными параметрами образующего треугольника и
    заданными координатами конца нитки с заданием угла поворота
    ----------------------------------------------------------
    x - горизонтальная координата центра основания образующего треугольника
    y - вертикальная координата центра основания образующего треугольника
    a - основание образующего треугольника
    h - высота образующего треугольника
    f - угол поворота фигуры
    xline - горизонтальная координата конца нитки
    yline - вертикальная координата конца нитки
    colors - кортеж цветов.
    '''
    draw_triangle(colors[0], x, y, a, h, f) 
    pgd.circle(screen, colors[1], (int(round(x +     a*np.cos(f)/2)), int(round(y -     a*np.sin(f)/2))), a//2) 
    pgd.circle(screen, colors[2], (int(round(x -     a*np.cos(f)/2)), int(round(y -     a*np.sin(f)/2))), a//2)
    pgd.circle(screen, colors[3], (int(round(x - 0.6*a*np.sin(f)  )), int(round(y - 0.6*a*np.cos(f)  ))), a//2)
    
    pgd.aalines(screen, colors[4], False, [[x + h*np.sin(f), y + h*np.cos(f)],
                                           [xline          , yline          ]])
    
    
def draw_heart(x, y, a, h, f, xline, yline, colors = [COLOR['Red'], COLOR['Black']]):
    '''
    Рисует шарик-сердечко с заданными параметрами образующего треугольника и
    заданными координатами конца нитки с заданием угла поворота
    ----------------------------------------------------------
    x - горизонтальная координата центра основания образующего треугольника
    y - вертикальная координата центра основания образующего треугольника
    a - основание образующего треугольника
    h - высота образующего треугольника
    f - угол поворота фигуры
    xline - горизонтальная координата конца нитки
    yline - вертикальная координата конца нитки
    colors - кортеж цветов.
    '''
    draw_triangle(colors[0], x, y, a, h, f)
    pgd.circle(screen, colors[0], (int(round(x + a*np.cos(f)/2)), int(round(y - a*np.sin(f)/2))), a//2) 
    pgd.circle(screen, colors[0], (int(round(x - a*np.cos(f)/2)), int(round(y - a*np.sin(f)/2))), a//2)
    
    pgd.aalines(screen, colors[1], False, [[x + h*np.sin(f), y + h*np.cos(f)],
                                           [xline          , yline          ]])

def background(colors = (COLOR['SkyBlue'], COLOR['ForestGreen']), y_sep = 300):
    '''
    Рисует фон с заданными цветами неба и земли
    ----------------------------------------------------------
    colors - кортеж цветов
    '''
    screen.fill(colors[0])
    pgd.rect(screen, colors[1], (0, y_sep, X, y_sep))
    
    
def boys(y_head, colors = (COLOR['Black'], COLOR['Human'], COLOR['Blue']), place = [1, 4]):
    '''
    Рисует мальчиков на заданных местах с фиксированным положением рук
    ----------------------------------------------------------
    y_head - координата макушки мальчика
    colors - кортеж цветов
    place - лист с номером положений мальчиков
    '''
    for i in place:
        for p in [-1, 1]:
            pgd.aalines(screen, colors[0], False, [[HUMAN['Dist']*i + p  *HUMAN['Head']/2  , y_head + 2.5*HUMAN['Head']    ],
                                                   [HUMAN['Dist']*i + p*3*HUMAN['Head']*0.9, y_head + 5  *HUMAN['Head']*0.9]])
    
            pgd.aalines(screen, colors[0], False, [[HUMAN['Dist']*i + p  *HUMAN['Head']/2, y_head + 3.3*HUMAN['Head']                    ],
                                                   [HUMAN['Dist']*i + p*5*HUMAN['Head']/8, y_head + 7  *HUMAN['Head']/2 + HUMAN['Height']],
                                                   [HUMAN['Dist']*i + p  *HUMAN['Head']  , y_head + 7  *HUMAN['Head']/2 + HUMAN['Height']]])
    
        pgd.ellipse(screen, colors[2], (HUMAN['Dist']*i - HUMAN['Head'], y_head + 3*HUMAN['Head']/2, 2*HUMAN['Head'], HUMAN['Height'])) 
        pgd.circle (screen, colors[1], (HUMAN['Dist']*i                , y_head +   HUMAN['Head']) , HUMAN['Head'])
    
    
def girls(y_head, colors = (COLOR['Black'], COLOR['Human'], COLOR['Pink']), place = [2, 3]):
    '''
    Рисует девочек на заданных местах с фиксированным положением рук
    ----------------------------------------------------------
    y_head - координата макушки девочки 
    colors - кортеж цветов
    place - лист с номером положений девочек
    '''
    for i in place:
        pgd.aalines(screen, colors[0], False, [[HUMAN['Dist']*i + (i - 2.5)*2 *HUMAN['Head']/2  , y_head + 2.5*HUMAN['Head']    ],
                                               [HUMAN['Dist']*i + (i - 2.5)*6 *HUMAN['Head']*0.9, y_head + 5  *HUMAN['Head']*0.9]])
    
        pgd.aalines(screen, colors[0], False, [[HUMAN['Dist']*i - (i - 2.5)*2 *HUMAN['Head']/2  , y_head + 2.5*HUMAN['Head']],
                                               [HUMAN['Dist']*i - (i - 2.5)*10*HUMAN['Head']/4  , y_head + 4  *HUMAN['Head']],
                                               [HUMAN['Dist']*i - (i - 2.5)*11*HUMAN['Head']/2  , y_head + 3  *HUMAN['Head']]]) 
        for p in [-1, 1]:
            pgd.aalines(screen, colors[0], False, [[HUMAN['Dist']*i + p  *HUMAN['Head']/2, y_head + 3.3*HUMAN['Head']                    ],
                                                   [HUMAN['Dist']*i + p*5*HUMAN['Head']/8, y_head + 7  *HUMAN['Head']/2 + HUMAN['Height']],
                                                   [HUMAN['Dist']*i + p  *HUMAN['Head']  , y_head + 7  *HUMAN['Head']/2 + HUMAN['Height']]])
    
        draw_triangle(        colors[2],  HUMAN['Dist']*i, y_head + 3*HUMAN['Head']/2 + HUMAN['Height'], 2*HUMAN['Head'], HUMAN['Height'], np.pi/1)
        pgd.circle   (screen, colors[1], (HUMAN['Dist']*i, y_head +   HUMAN['Head'])                   , HUMAN['Head'])
 
    
    
background()
draw_flavour(400, 100, 40, 80, np.pi/20, 400, 340)
draw_flavour(750, 320, 20, 40, -np.pi/15, 720, 385)
draw_heart(50, 200, 30, 60, 0, 80, 385)
boys(250)
girls(250)      

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


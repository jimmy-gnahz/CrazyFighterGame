import pygame
#from Street_Fighter_Game1 import *
"///color values///"
BLACK = [  0,   0,   0]
WHITE = [255, 255, 255]
RED = [255, 0 , 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
GREEN = [ 0 , 255 , 0 ]
"///other values///"
size = [1000,644]
screen = pygame.display.set_mode(size)

def draw_player(x,y):
    pygame.draw.polygon(screen,BLUE, [[ 100 + x, 0 + y ], [0 + x, 50 + y], [200 + x, 50 + y]], 0) 
    pygame.draw.circle(screen,BLUE, [100 + x, 75 + y], 50)
    pygame.draw.rect(screen, BLUE, [50 + x, 120 + y, 100, 200])
    pygame.draw.rect(screen, BLUE, [50 + x, 320 + y, 30, 100])
    pygame.draw.rect(screen, BLUE, [120 + x, 320 + y, 30, 100]) 
    #arm 
    pygame.draw.rect(screen, BLUE, [150 + x, 150 + y, 50, 50])    
    #wand
    pygame.draw.polygon(screen,BLACK, [[ 255 + x, 55 + y ], [275 + x, 75 + y], [200 + x, 150+ y], [150 + x, 150 + y]], 0)     
    pygame.draw.circle(screen,YELLOW, [275 + x, 50 + y], 25)
 
def draw_enemy(a,b): 
    pygame.draw.polygon(screen,BLACK, [[ 10 + a, 150 + b ], [20 + a, 20 + b], [30 + a, 150 + b]], 0) 
    pygame.draw.circle(screen,RED, [100 + a, 75 + b], 50) 
    pygame.draw.rect(screen, RED, [50 + a, 120 + b, 100, 200])
    pygame.draw.rect(screen, RED, [50 + a, 320 + b, 30, 100])
    pygame.draw.rect(screen, RED, [120 + a, 320 + b, 30, 100])
    pygame.draw.rect(screen, RED, [0 + a, 150 + b, 50, 50])    
    pygame.draw.rect(screen, BLACK, [10 + a, 200 + b, 20, 20])
    
def draw_fireball(x):
    pygame.draw.circle(screen,RED, [x, 250],int((fireball_x - 275)/3.0))
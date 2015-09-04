# Author : Philip Xia, Jimmy Zhang

#//////////////////////////////////////////////////////////////////////////////#
#                                                                              #
#                                                                              #
#                                                                              #
#                            Street Fighter Game                               #
#                                                                              #
#                                                                              #
#                                                                              #
#//////////////////////////////////////////////////////////////////////////////#

#import libraries
import pygame
import sys
from random import randint
from models import *
"/////////////background import/////////////////////"
pygame.init()

background = pygame.image.load("background.png")

#///////////////////////////////////////////////////#
#                                                   #
#                Define values                      #
#                                                   #
#///////////////////////////////////////////////////#
 
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
done = False
clock = pygame.time.Clock()
player_x = 0 
enemy_x = 800
hit_enemy = False
fireball_x = 275
draw_fireball_trigger = False 
move_forward_trigger = False
move_backward_trigger = False
player_text ="100/100"
enemy_text = "125/125"
player_mana_text = "100/100"
enemy_mana_text = "100/100"
#game values
player_hp = 100
player_mana = 80
enemy_hp = 125
player_physical_damage = 20
player_magic_damage = randint(20,40)
player_magic_mana_usage = 30
player_ultimate_damage = randint(30,50) 
player_ultimate_mana_usage = 50
game_over = False
enemy_p_damage = 15
    
#///////////////////////////////////////////////////#
#                                                   #
#                   Main Loop                       #
#                                                   #
#///////////////////////////////////////////////////#
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 

 

           
#/////////////////////screen color/////////////////////#
    screen.fill(BLACK)
    screen.blit(background, (0,0))    
    draw_player(player_x,200)
    draw_enemy(enemy_x, 200)
    
# font
    player_text = str(player_hp) + "/100"
    myfont = pygame.font.SysFont("monospace", 20, True)
    label = myfont.render(player_text, 1, RED)
    screen.blit(label, (5, 50))
    
    enemy_text = str(enemy_hp) + "/125"
    label2 = myfont.render(enemy_text, 1, RED)
    screen.blit(label2, (840, 50))
    
    label3 = myfont.render(player_mana_text, 1, BLUE)
    screen.blit(label3, (5, 150))
    
    label4 = myfont.render(enemy_mana_text, 1, BLUE)
    screen.blit(label4, (840, 150))    

#////////////////////magic attack trigger//////////////#
    pygame.display.flip()
 
    clock.tick(60)
     
#///quit///#     
pygame.quit ()
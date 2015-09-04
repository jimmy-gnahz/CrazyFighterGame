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
#values
pygame.init()
background = pygame.image.load("background.png")
enemy_hp = 125
player_hp = 100
 
#///////////////////////////////////////////////////#
#                                                   #
#                   Main Loop                       #
#                                                   #
#///////////////////////////////////////////////////#
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                move_forward_trigger = True
                
                
            #elif event.key == pygame.K_w:
                
            #elif event.key == pygame.K_r:
        
    if move_forward_trigger == True:
        player_x += 25
        if player_x >= 500:
            move_forward_trigger = False
            enemy_hp -= 20
            move_backward_trigger = True
    if move_backward_trigger == True:
        player_x -= 25
        if player_x <= 0:
            move_backward_trigger = False
#/////////////////////Functions/////////////////////#
    screen.fill(BLACK)
    screen.blit(background, (0,0))    
    draw_player(player_x,200)
    draw_enemy(enemy_x, 200)
    draw_font(player_hp,enemy_hp)
#///////////////////end//////////////#
    pygame.display.flip()
 
    clock.tick(60)
     
#///quit///#     
pygame.quit ()
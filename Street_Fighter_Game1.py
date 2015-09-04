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
damage = 0 
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
            
            #///////////////////////////////////// TODO
            atk_trigger = True
            damage = randint(20,40)
            
            #//////////////////////////////////// END
            
            if event.key == pygame.K_q:
                move_forward_trigger = True
                
            #///////////////////////////////////// TODO    
            #elif event.key == pygame.K_w:
                
            #elif event.key == pygame.K_r:
            #//////////////////////////////////// END
        
    if move_forward_trigger == True:
        
        player_x += 25
        if player_x >= 500:
            move_forward_trigger = False
            enemy_hp -= 20
            move_backward_trigger = True
    if move_backward_trigger == True:
        player_x -= 25
        if player_x <= 0:
            atk_trigger = False
            move_backward_trigger = False
            player_hp -= damage #/////////////////////////////////// NOTE
            
            
            
            
            
            
            
            
            
            
            
            
#/////////////////////Functions/////////////////////#
    screen.fill(BLACK)
    screen.blit(background, (0,0))    
    draw_player(player_x,200)
    draw_enemy(enemy_x, 200)
    draw_hp_font(player_hp,enemy_hp)
    if atk_trigger == False: 
        draw_game_msg_font(damage, "Physical") #////////////////////// TODO
#///////////////////end//////////////#
    pygame.display.flip()
 
    clock.tick(60)
     
#///quit///#     
pygame.quit ()
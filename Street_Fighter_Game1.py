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

 
#////////////////////////////////////////////////////#
#                                                    #
#                FUNNCTION DEFINITIONS               #
#                                                    #
#////////////////////////////////////////////////////#

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
    
#///////////////////////////////////////////////////#
#                                                   #
#                   Main Loop                       #
#                                                   #
#///////////////////////////////////////////////////#
while not game_over:
    player_magic_damage = randint(20,40)
    player_ultimate_damage = randint(30,50) 
    player_mana = player_mana + 20 
    if player_mana > 100:
        player_mana = 100 
    # display current hp
    print "your hp: " + str(player_hp)
    print "enemy hp: " + str(enemy_hp)    
    print "your mana: " + str(player_mana)    
    
    
    # player attack

    if atk_choice == pygame.K_q:

        crit_number = randint(1,4)
        if crit_number != 1:
            enemy.hp = enemy.hp - player_physical_damage
        else:
            enemy.hp = enemy.hp - player_physical_damage * 2
            print "*****Crit*****"
          
    elif atk_choice == pygame.keydown_r: 
        #speed when moving forwards    
        if move_forward_trigger == True:
            player_x += 25
        #trigger
        if player_x >= 500: 
            enemy_hp -= 20
            move_forward_trigger = False   
            move_backward_trigger = True
        #speed when moving backwards
        if move_backward_trigger == True:
            player_x -= 25
        #stop moving backwards
        if player_x <= 0:
            move_backward_trigger = False        
        if player_mana < player_ultimate_mana_usage:
            player_ultimate_damage = 0 
            print "^^^^^Not enough mana^^^^^";
        elif player_mana >= player_ultimate_mana_usage:
            enemy_hp = enemy.hp - player_ultimate_damage
            player_mana = player_mana - player_ultimate_mana_usage            
        
    elif atk_choice == pygame.keydown_w:
        if draw_fireball_trigger == True:
            draw_fireball(fireball_x)        
        #speed of fireball                                      
        if draw_fireball_trigger == True:
            fireball_x += 25
        #fireball disappears    
        if fireball_x >= 800: 
            draw_fireball_trigger = False
            fireball_x = 275       
            
        if player_mana < player_magic_mana_usage:
            player_magic_damage = 0    
            print "^^^^^Not enough mana^^^^^"
        elif player_mana >= player_magic_mana_usage:
            player_mana = player_mana - player_magic_mana_usage
        
        miss_number = randint(1,3)
        if miss_number == 1:
            enemy.hp = enemy.hp
            print "~~~~~The enemy has evaded your atk~~~~~"
        else:    
            enemy.hp = enemy.hp - player_magic_damage
            
    elif atk_choice == "quit":
        break
    
    else:
        continue 
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
      
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if not hit_enemy:
                    draw_fireball_trigger = True
                    
            if event.key == pygame.K_q:
                move_forward_trigger = True
    # enemy attack
    enemy_atk = randint(0,1) # 0 is physical, 1 is magic
    if enemy_atk == 0:
        player_hp = player_hp - enemy.p_damage
    elif enemy_atk == 1:
        miss_number = randint(1,3)
        if miss_number == 1:
            print "~~~~~You have evaded the enemy's atk~~~~~"
            player_hp = player_hp
        else:    
            player_hp = player_hp - randint(15,35)        
    
    
    #speed of fireball                                      
    if draw_fireball_trigger == True:
        fireball_x += 25
    #fireball disappears    
    if fireball_x >= 800: 
        draw_fireball_trigger = False
        fireball_x = 275

           
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
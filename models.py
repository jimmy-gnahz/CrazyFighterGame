import pygame
from random import randint

#colors
BLACK = [  0,   0,   0]
WHITE = [255, 255, 255]
RED = [255, 0 , 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
GREEN = [ 0 , 255 , 0 ]
#values
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
player_mana = 80
player_physical_damage = 20
player_magic_damage = randint(20,40)
player_magic_mana_usage = 30
player_ultimate_damage = randint(30,50) 
player_ultimate_mana_usage = 50
game_over = False
enemy_p_damage = 15
atk_trigger = True

#draw 
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

#font
def draw_hp_font(player_hp,enemy_hp):
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

def draw_game_msg_font(damage,atk_type):
    myfont = pygame.font.SysFont("monospace", 20, True)
    message = "Enemy dealt " + str(damage) + " damage to you " + atk_type
    label5 = myfont.render(message, 1, RED)
    screen.blit(label5, (300, 50))
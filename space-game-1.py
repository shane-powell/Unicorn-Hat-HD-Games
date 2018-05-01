#! /usr/bin/python

import unicornhathd
import pygame, time, random
from pygame.locals import *

#Initialise pygame.
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 10))
pygame.display.set_caption('Pygame Window')
pygame.mouse.set_visible(0)

#Initialise unicorn hat.
unicornhathd.rotation(90)
unicornhathd.brightness(1)
u_width,u_height = unicornhathd.get_shape()
xPixels = 16
yPixels = 16

#The maximum number of projectiles a player can have active at once.
maxProjectiles = 3

#Array of player projectiles.
projs = []

#Arry of enemies.
enemies = []

#Array of enemy projectiles.
enProjs = []

#Represents a projectile from player or enemy.
class Proj:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Represents an enemy in the game
class Enemy:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.alive = True

#Creates a new enemy
def CreateEnemy(x, y, d):
    e = Enemy(x, y, d)
    enemies.append(e);

#Draw all alive enemies and decides if they should fire
def DrawEnemies():
    for e in enemies:
        if(e.alive):
        
            if(e.x <= 0):
                e.dir = 'r'
                e.y -= 1
            elif(e.x >= xPixels -1):
                e.dir = 'l'
                e.y -= 1
       
            if(e.dir == 'r'):
                e.x += 1
            else:
                e.x -= 1
                          
            unicornhathd.set_pixel(e.x, e.y, 255, 0, 0)
            #Randomly decide whether enemy should fire
            if(random.randint(1, 20) == 1):
                #Fire
                eP = Proj(e.x, e.y -1)
                enProjs.append(eP)
        else:
            enemies.remove(e)  
    
    return

#Draws the player ship
def DrawShip(): 
    unicornhathd.set_pixel(shipX, shipY, 255, 255, 0)  
    return

#TODO: Move game launch into its on method.
#def StartGame():


try:
    #Create initial game state.
    shipX = 7
    shipY = 0
    
    #Create enemies
    CreateEnemy(1, 15, 'r')
    CreateEnemy(5, 14, 'l')
    CreateEnemy(10, 13, 'r')
    gameRunning = True
    while gameRunning == True:
        #Set game loop speed
        clock.tick(15)
        
        #Check for and process new keyboard events
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if event.key == pygame.K_LEFT:
                    if(shipX > 0):
                        shipX -= 1
                elif event.key == pygame.K_RIGHT:
                    if(shipX < yPixels - 1): 
                        shipX += 1
                
                if event.key == pygame.K_SPACE:
                    print(len(projs))
                    if(len(projs) < 3):
                        p = Proj(shipX, shipY +1)
                        projs.append(p)                                  
    
        unicornhathd.clear()
        
        #Draw Player
        DrawShip();
        #Draw Enemys
        DrawEnemies();
        
        
        # Process player projectiles
        for p in projs:
            if(p.y < yPixels -1):
                p.y +=1
                #Check for collision between player projectile and enemies
                for e in enemies:
                    if(e.alive):
                        if(p.y == e.y and p.x == e.x):
                            e.alive = False
                # Draw player projectile    
                unicornhathd.set_pixel(p.x, p.y, 0, 0, 255)
            else:
                projs.remove(p)
        
        # Process enemy projectiles
        for p in enProjs:
            if(p.y > 0):
                p.y -=1
                
                # Check for collision between enemy projectile and player.
                if(p.x == shipX and p.y == shipY):
                    gameRunning = False
                    print("game over");   
                # Draw Enemy projectile        
                unicornhathd.set_pixel(p.x, p.y, 0, 255, 255)
            else:
                enProjs.remove(p)
        
        # Check for collision between player and enemy
        for e in enemies:
            if(e.x == shipX and e.y == shipY):
                gameRunning = False
                print("game over");             
        unicornhathd.show()
        
    unicornhathd.clear()
    #TODO Show game over text
    unicornhathd.show();
    time.sleep(10);

                
except KeyboardInterrupt:
    #Close down unicorn hat and pygame
    unicornhathd.clear()
    unicornhathd.off()
    pygame.quit()
            

#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block

import unicornhathd
import pygame, time
from pygame.locals import *



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 10))
pygame.display.set_caption('Pygame Window')
pygame.mouse.set_visible(0)

unicornhathd.rotation(90)
unicornhathd.brightness(1)
u_width,u_height = unicornhathd.get_shape()



xPixels = 16
yPixels = 16

shotX = 0
shotY = 0
shotActive = False

class Enemy:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.alive = True
        
en1 = Enemy(1, 15, 'r')

def DrawEnemies():
    
    
    if(en1.alive):
        
        if(en1.x <= 0):
            en1.dir = 'r'
        elif(en1.x >= xPixels -1):
            en1.dir = 'l'
       
        if(en1.dir == 'r'):
            en1.x += 1
        else:
            en1.x -= 1
            
    
        unicornhathd.set_pixel(en1.x, en1.y, 255, 0, 0)
    
    
    return

def DrawShip(): 
    unicornhathd.set_pixel(shipX, shipY, 255, 255, 0)
    
    if(shotActive == True):
        unicornhathd.set_pixel(shotX, shotY, 0, 0, 255)
    
    return

try:
    shipX = 7
    shipY = 0
    while True:
        #http://qq.readthedocs.io/en/latest/main_loop.html
        #print("loop")
        clock.tick(15)
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if event.key == pygame.K_LEFT:
                    shipX -= 1
                elif event.key == pygame.K_RIGHT:
                    shipX += 1
##                elif event.key == pygame.K_UP:
##                    shipY += 1
##                elif event.key == pygame.K_DOWN:                        
##                    shipY -= 1
                
                if event.key == pygame.K_SPACE:
                    shotX = shipX
                    shotY = shipY + 1
                    shotActive = True
                
    
        unicornhathd.clear()
        #print(shipY)
        DrawShip();
        DrawEnemies()
        
        if(shotY < yPixels -1):
            shotY +=1
            if(shotY == en1.y and shotX == en1.x):
                en1.alive = False
        else:
            shotActive = False
                     
        unicornhathd.show()
                
except KeyboardInterrupt:
    unicornhathd.clear()
    unicornhathd.off()
            

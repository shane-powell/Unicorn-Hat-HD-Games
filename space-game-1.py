#! /usr/bin/python

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

maxProjectiles = 3
projs = []
enemies = []

class Proj:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Enemy:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.alive = True
        
e = Enemy(1, 15, 'r')
enemies.append(e);

def DrawEnemies():
    
    for e in enemies:
        if(e.alive):
        
            if(e.x <= 0):
                e.dir = 'r'
            elif(e.x >= xPixels -1):
                e.dir = 'l'
       
            if(e.dir == 'r'):
                e.x += 1
            else:
                e.x -= 1
            
    
            unicornhathd.set_pixel(e.x, e.y, 255, 0, 0)
        else:
            enemies.remove(e)  
    
    return

def DrawShip(): 
    unicornhathd.set_pixel(shipX, shipY, 255, 255, 0)  
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
                    if(shipX > 0):
                        shipX -= 1
                elif event.key == pygame.K_RIGHT:
                    if(shipX < yPixels - 1): 
                        shipX += 1
##                elif event.key == pygame.K_UP:
##                    shipY += 1
##                elif event.key == pygame.K_DOWN:                        
##                    shipY -= 1
                
                if event.key == pygame.K_SPACE:
                    print(len(projs))
                    if(len(projs) < 3):
                        p = Proj(shipX, shipY +1)
                        projs.append(p)                                  
    
        unicornhathd.clear()
        DrawShip();
        DrawEnemies();
        
        for p in projs:
            if(p.y < yPixels -1):
                p.y +=1
                for e in enemies:
                    if(e.alive):
                        if(p.y == e.y and p.x == e.x):
                            e.alive = False
                        
                unicornhathd.set_pixel(p.x, p.y, 0, 0, 255)
            else:
                projs.remove(p)

        
        #if(shotY < yPixels -1):
        #    shotY +=1
        #    if(shotY == en1.y and shotX == en1.x):
        #       en1.alive = False
       # else:
        #    shotActive = False
                     
        unicornhathd.show()
                
except KeyboardInterrupt:
    unicornhathd.clear()
    unicornhathd.off()
            

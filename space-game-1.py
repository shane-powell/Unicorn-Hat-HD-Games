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
        
def CreateEnemy(x, y, d):
    e = Enemy(x, y, d)
    enemies.append(e);

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
        else:
            enemies.remove(e)  
    
    return

def DrawShip(): 
    unicornhathd.set_pixel(shipX, shipY, 255, 255, 0)  
    return

try:
    shipX = 7
    shipY = 0
    
    CreateEnemy(1, 15, 'r')
    CreateEnemy(5, 14, 'l')
    CreateEnemy(10, 13, 'r')
    gameRunning = True
    while gameRunning == True:
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
        
        for e in enemies:
            if(e.x == shipX and e.y == shipY):
                gameRunning = False
                print("game over");             
        unicornhathd.show()
        
    unicornhathd.clear()
    #Show game over
    unicornhathd.show();
    time.sleep(10);

                
except KeyboardInterrupt:
    unicornhathd.clear()
    unicornhathd.off()
    pygame.quit()
            

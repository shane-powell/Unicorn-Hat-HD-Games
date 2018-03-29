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
        
        if(shotY < yPixels -1):
            shotY +=1
        else:
            shotActive = False
                     
        unicornhathd.show()
                
except KeyboardInterrupt:
    unicornhathd.clear()
    unicornhathd.off()
            

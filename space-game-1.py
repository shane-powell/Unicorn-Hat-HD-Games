#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block

import unicornhathd
import pygame, time
from pygame.locals import *

shipX = 7
shipY = 7

pygame.init()
screen = pygame.display.set_mode((300, 10))
pygame.display.set_caption('Pygame Window')
pygame.mouse.set_visible(0)

unicornhathd.rotation(0)
unicornhathd.brightness(1)
u_width,u_height = unicornhathd.get_shape()



xPixels = 16
yPixels = 16

def DrawShip(): 
    unicornhathd.set_pixel(shipX, shipY, 255, 255, 0)
    return

try:
    while True:
        print("loop")
        for event in pygame.event.get():
            if (event.type == KEYUP):
                shipY -= 1
            elif (event.type == KEYDOWN):
                shipY += 1
                
    
        unicornhathd.clear()
        print(shipY)
        DrawShip();
            
                     
        unicornhathd.show()
                
except KeyboardInterrupt:
    unicornhathd.off()
            

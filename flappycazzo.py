# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:41:44 2022

@author: GATTO
"""

#
import pygame
import random

pygame.init() 

#sfondo = pygame.image.load('')

#personaggio = pygame.image.load('')
#base = pygame.image.load('')
#gameover = pygame.image.load('')
#tubo_giu = pygame.image.load('')
#tubo_su = pygame.transform.flip(tubo_giu,False,True)

schermo = pygame.display.set_mode((288, 512))

Fps = 50

def inizializza():
    global uccellox,uccelloy,uccello_vely
    uccellox,uccelloy = 60,150
    uccello_vely = 0
    
inizializza()

while True:
    uccello_vely +=1
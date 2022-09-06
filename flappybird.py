# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:41:44 2022

@author: GATTO ma pure Alessio
"""

#
import os
import pygame
import random

pygame.init() 

pathImg = os.path.dirname("Videogioco/assets/img/soap-bubble.jpg")
bollaSapone = os.path.join(pathImg, "soap-bubble.jpg")
occhiGatto = os.path.join(pathImg, "cats-eyes.jpg")

player = pygame.image.load(bollaSapone)
sfondo = pygame.image.load(occhiGatto)

#base = pygame.image.load('')
#gameover = pygame.image.load('')
#tubo_giu = pygame.image.load('')
#tubo_su = pygame.transform.flip(tubo_giu,False,True)

info = pygame.display.Info() 
screenWidth,screenHeight = info.current_w,info.current_h
SCHERMO = pygame.display.set_mode((screenWidth - 10, screenHeight - 50), pygame.RESIZABLE)
#SCHERMO = pygame.display.set_mode((screenWidth - 10, screenHeight - 50), pygame.FULLSCREEN)
FPS = 50

def inizializza():
    global playerX,playerY,playerVelY
    playerX,playerY = 60,150
    playerVelY = 0
    
inizializza()

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(player, (playerX, playerY))

while True:
    playerVelY +=1
    playerY += playerVelY
    disegna_oggetti()
    aggiorna()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
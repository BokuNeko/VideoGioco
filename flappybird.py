# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:41:44 2022

@author: GATTO ma pure Alessio
"""

#
import os
from sys import path_importer_cache
import pygame
import random

pygame.init() 

pathImg = os.path.dirname("Videogioco/assets/img/soap-bubble.jpg")
###Carico le immagini###
pathImg = os.path.dirname("assets/img/soap-bubble.jpg")
bollaSapone = os.path.join(pathImg, "soap-bubble.jpg")
occhiGatto = os.path.join(pathImg, "cats-eyes.jpg")
lightblue = os.path.join(pathImg, "base.png")
gameover = os.path.join(pathImg, "gameover.png")

player = pygame.image.load(bollaSapone)
sfondo = pygame.image.load(occhiGatto)

base = pygame.image.load(lightblue)
gameover = pygame.image.load('')
#tubo_giu = pygame.image.load('')
#tubo_su = pygame.transform.flip(tubo_giu,False,True)


###Dimensioni della finestra di gioco
info = pygame.display.Info() 
screenWidth,screenHeight = info.current_w,info.current_h
SCHERMO = pygame.display.set_mode((screenWidth, screenHeight - 50), pygame.RESIZABLE)
#SCHERMO = pygame.display.set_mode((screenWidth, screenHeight - 50), pygame.FULLSCREEN)
FPS = 50
VELX = 5
#Dimensioni della base
HBASE = screenHeight - (screenHeight / 6)
WBASE = (screenWidth - screenWidth / 5)

def inizializza():
    global playerX,playerY,playerVelY,baseX
    #Posizione iniziale del personaggio
    playerX,playerY = 60,150
    #Velocità iniziale del personaggio (caduta)
    playerVelY = 0
    baseX = 0
    
inizializza()

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def disegna_oggetti():
    pygame.Surface.fill(SCHERMO, (0, 0, 0))
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(player, (playerX, playerY))
    SCHERMO.blit(base, (baseX, HBASE))

def hai_perso():
    SCHERMO.blit(gameover,(50,))

###Ciclo per la caduta del personaggio###
while True:
    baseX -= VELX
    if(baseX <= - WBASE):
        baseX = 0
        
    if(playerY <= (HBASE - 70)):
        playerVelY += 0.5
        playerY += playerVelY
        
    disegna_oggetti()
    aggiorna()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            playerVelY = - 10
            playerY += playerVelY

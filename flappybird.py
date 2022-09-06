# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:41:44 2022

@author: GATTO ma pure Alessio LOL
"""

#
import os
import pygame
import random

pygame.init() 

###Carico le immagini###
pathImg = os.path.dirname("Videogioco/assets/img/soap-bubble.jpg")
bollaSapone = os.path.join(pathImg, "soap-bubble.jpg")
occhiGatto = os.path.join(pathImg, "cats-eyes.jpg")
lightblue = os.path.join(pathImg, "base.png")

###Assegno le immagini
player = pygame.image.load(bollaSapone)
sfondo = pygame.image.load(occhiGatto)
base = pygame.image.load(lightblue)
#gameover = pygame.image.load('')
#tubo_giu = pygame.image.load('')
#tubo_su = pygame.transform.flip(tubo_giu,False,True)

###Ottengo informazioni sullo schermo
info = pygame.display.Info() 
screenWidth,screenHeight = info.current_w,info.current_h
SCHERMO = pygame.display.set_mode((screenWidth, screenHeight - 50), pygame.RESIZABLE)
#SCHERMO = pygame.display.set_mode((screenWidth, screenHeight - 50), pygame.FULLSCREEN)

###Costanti Globali
FPS = 50
VELX = 5
HBASE = screenHeight - (screenHeight / 6)
WBASE = (screenWidth - screenWidth / 5)

def inizializza():
    global playerX,playerY,playerVelY,baseX
    playerX,playerY = 60,150
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

###Ciclo per la caduta del personaggio###
while True:
    #Movimento della base verso sx (illusiione di movimento)
    baseX -= VELX
    #Loop della base
    if(baseX <= - WBASE):
        baseX = 0
    
    #Gravità (ad ogni ciclio il personaggio cade più velocemente)    
    if(playerY <= (HBASE - 70)):
        playerVelY += 0.5
        playerY += playerVelY
        
    disegna_oggetti()
    aggiorna()

    #Gestione degli eventi
    for event in pygame.event.get():
        #Spegne il gioco
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Se premo spazio il personaggio sale
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            #La velocità negativa diminuisce la discesa
            playerVelY = - 10
            playerY += playerVelY

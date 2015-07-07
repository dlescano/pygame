#!/usr/bin/env python
# -*- coding: utf-8 -*-

#modulos importados
import pygame
import sys
from pygame.locals import *
from personaje import *
from mapa import *
from personaje import *
from data import *

#funcion principal
def main():
    mapa = Mapa(largo,ancho)
    mapa.load_mapa(datos_fondo)
    mapa.cargar_mapa()
    pantalla = pygame.display.set_mode((640,480))
    color = (255,255,255)
    reloj = pygame.time.Clock()
    player = Personaje(200,230)
    while True:
        pantalla.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        mapa.dibujar_mapa(pantalla)
        player.handle_event(event)
        pantalla.blit(player.parte,player.rect)

        pygame.display.flip()
        reloj.tick(15)
    pygame.quit()

#****************** se ejecuta el juego **********************
if __name__ == '__main__':
    pygame.init()
    main()
#*************************************************************
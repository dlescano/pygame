import pygame, sys
from pygame.locals import *

class Mapa(object):
    """docstring for Mapa"""
    def __init__(self, largo, ancho):
        self.piso0 = pygame.image.load("graficos/mapas/mapa0/piso-negro0.gif")
        self.piso1 = pygame.image.load("graficos/mapas/mapa0/piso-negro1.gif")
        self.piso2 = pygame.image.load("graficos/mapas/mapa0/piso-negro3.gif")
        self.piso3 = pygame.image.load("graficos/mapas/mapa0/piso-negro4.gif")
        #self.rect_mosaico = self.mosaico.get_rect()
        self.size_tiles = 32
        self.ancho = ancho
        self.largo = largo
        self.cantidad_ancho = 480/32
        self.cantidad_largo = 640/32
        self.dict_mapa = []

    def load_mapa(self, ruta):
        self.archivo = open(ruta, "r")

    def cargar_mapa(self):
        i = 0
        for linea in self.archivo.readlines():
            l_linea = linea.split()
            self.dict_mapa.append(l_linea)

    def dibujar_mapa(self, pantalla):
        moverxDERECHA = 0
        moverxABAJO = 0
        for fila in self.dict_mapa:
            for elem in fila:
                if int(elem) == 0:
                    pantalla.blit(self.piso0,(moverxABAJO,moverxDERECHA))
                elif int(elem) == 1:
                    pantalla.blit(self.piso1,(moverxABAJO,moverxDERECHA))
                elif int(elem) == 2:
                    pantalla.blit(self.piso2,(moverxABAJO,moverxDERECHA))
                elif int(elem) == 3:
                    pantalla.blit(self.piso3,(moverxABAJO,moverxDERECHA))
                moverxABAJO += self.size_tiles
            moverxDERECHA += self.size_tiles
            moverxABAJO = 0

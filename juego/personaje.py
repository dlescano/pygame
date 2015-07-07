# -*- coding: utf-8 -*-
#modulos importados
import pygame
from pygame.locals import *
#--------------------------------- CLASES ---------------------------------------------------
class Personaje(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        #cargo el fotograma con todas las pociones del personaje
        self.imagen = pygame.image.load("graficos/campeones/VX0.png")
        #le paso a la variable parte el tamaño de los rectangulos (32x32)
        self.imagen.set_clip(pygame.Rect(0,0,32,32))
        self.parte = self.imagen.subsurface(self.imagen.get_clip())
        #creo el rectangulo a partir de los datos de parte
        self.rect = self.parte.get_rect()

        #achico dicho rectangulo para que se vea como si de verdad
        #se toca el vorde del obj con el que hace colision
        self.rect.inflate_ip(-5,-10)
        #valor de las posiciones
        self.rect.top = y
        self.rect.left = x

        #el primer frame de mi fotograma
        self.frame = 0
        #------- cada uno de los cortes del fotograma segun su orientacion -------------- #
        self.left_states = { 0: (0, 32, 32, 32), 1: (32, 32, 32, 32), 2: (64, 32, 32, 32) }
        self.right_states = { 0: (0, 64, 32, 32), 1: (32, 64, 32, 32), 2: (64, 64, 32, 32) }
        self.up_states = { 0: (0, 96, 32, 32), 1: (32, 96, 32, 32), 2: (64, 96, 32, 32) }
        self.down_states = { 0: (0, 0, 32, 32), 1: (32, 0, 32, 32), 2: (64, 0, 32, 32) }
        #-----------------------------------------------------------------------------------#
        self.velocidad = 7
    #funcion que cambia el corte del fotograma a medida que el personaje se mueve
    #en una direccion
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    #crea la animacion
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.imagen.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    #funcion que se encarga de mover al personaje
    def update(self, direccion):
        if direccion == 'left':
            if self.rect.left > 0:
                self.rect.left -= self.velocidad
                self.clip(self.left_states)
        if direccion == 'right':
            if self.rect.right < 640:
                self.rect.left += self.velocidad
                self.clip(self.right_states)
        if direccion == 'up':
            if self.rect.top > 0:
                self.rect.top -= self.velocidad
                self.clip(self.up_states)
        if direccion == 'down':
            if self.rect.top < 440:
                self.rect.top += self.velocidad
                self.clip(self.down_states)
        #aca se muestra el frame inicial cuando se levanta la tecla pulsada
        if direccion == 'stand_left':
            self.clip(self.left_states[1])
        if direccion == 'stand_right':
            self.clip(self.right_states[1])
        if direccion == 'stand_up':
            self.clip(self.up_states[1])
        if direccion == 'stand_down':
            self.clip(self.down_states[1])
        self.parte = self.imagen.subsurface(self.imagen.get_clip())
    #funcion que detecta los eventos que son del tipo teclado
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
#*******************************************************

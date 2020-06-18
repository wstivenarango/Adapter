import pygame
from pygame.sprite import Sprite
from pygame import *
import util


class Mario(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.velocidad = 1
        #self.posX = 410
        #self.posY = 560

    def defPositions(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY

    def set_sprites(self, sprite):
        self.imagenes = sprite

    def moverDerecha(self):
        self.image = util.cargar_imagen('imagenes/mario_right.png')
        self.posX += self.velocidad
        
        
    def moverIzquierda(self):
        self.image = util.cargar_imagen('imagenes/mario_left.png')
        self.posX -= self.velocidad
    
    def update(self,sprite):
        self.image= util.cargar_imagen('imagenes/mario.png')      
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.moverIzquierda()
        if teclas[K_RIGHT]:
            self.moverDerecha() 
        

    def draw(self, screen):
        screen.blit(self.image, (self.posX,self.posY))
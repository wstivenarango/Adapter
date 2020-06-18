import pygame
from pygame.sprite import Sprite
from pygame import *
import util
class Personaje():
    def __init__(self):
        Sprite.__init__(self)
        self.velocidad = 1

    def defPositions(self, auxPosX, auxPosY):
        pass
        
    def moverDerecha(self):
        pass
                
    def moverIzquierda(self):
        pass   
    
    def update(self,sprite):
        pass
        
    def draw(self, screen):
        pass

class Dragon(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.velocidad = 1

    def Posic(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY
        
    def set_sprites(self, sprite):
        self.imagenes = sprite

    def Dere(self):
        self.image = util.cargar_imagen('imagenes/d1.png')
        self.posX += self.velocidad
                
    def Izq(self):
        self.image = util.cargar_imagen('imagenes/i1.png')
        self.posX -= self.velocidad      
    
    def actualizar(self,sprite):
        self.image= util.cargar_imagen('imagenes/d2.png')      
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.Izq()
        if teclas[K_RIGHT]:
            self.Dere()
        
    def dibujo(self, screen):
        screen.blit(self.image, (self.posX,self.posY))



class Adaptador(Dragon, Personaje):
    
    def moverDerecha(self):
        self.Dere()

    def moverIzquierda(self):
        self.izq()
        
    def update(self,sprite):
        self.actualizar(sprite)

    def draw(self, screen):
        self.dibujo(screen)

    def defPositions(self, auxPosX, auxPosY):
        self.Posic(auxPosX, auxPosY)
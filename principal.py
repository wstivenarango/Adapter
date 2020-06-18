import sys
import pygame
import util
from adaptado import Adaptador
from pygame.locals import *
from personaje import *


def game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    pygame.display.set_caption("adapter")
    background_image = util.cargar_imagen('imagenes/fondo.jpg')
    pygame.mouse.set_visible(False)
    ejecutando = True
    jugando = True 
    a = int(input("Ingrese 1: Para utilizar Mario\nIngrese 2: Para utilizar Dragon \n"))
    if a==1:
        posX=410
        posY=560
        heroe = Mario()
        heroe.defPositions(posX,posY)
        while ejecutando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ejecutando = False
                    sys.exit()
            screen.blit(background_image, (0,0))
            if jugando:
                heroe.update(sprite)
                heroe.draw(screen)
            pygame.display.update()  
    if a==2:
        posX=200
        posY=200
        adaptado = Adaptador()
        adaptado.defPositions(posX,posY) 
        while ejecutando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ejecutando = False
                    sys.exit()
            screen.blit(background_image, (0,0))
            if jugando:
                adaptado.update(sprite)
                adaptado.draw(screen)
            pygame.display.update()  

if __name__ == '__main__':
    game()


import pygame
import os



class Cubo:
    def __init__(self):
        self.image = pygame.image.load(os.path.join('imagen1.png')).convert()
        self.rect = pygame.Rect(0,0,100,100)
        self.rect.center = (800, 700)
        self.rect.centerx = 100
        
    def salto(self, jump, jumpCount, jumpMax):
        if jump: #logica de animacion del salto
            self.rect.y -= jumpCount
            if jumpCount > -jumpMax:
                jumpCount -= 1
            else:
                jump = False
        
        return (jump, jumpCount)         
        


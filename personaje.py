import pygame
import os



class Cubo:
    def __init__(self):
        self.image = pygame.image.load(os.path.join('imagen1.png')).convert()
        self.rect = pygame.Rect(100,660,100,100)
        
    def salto(self, jump, jumpCount, jumpMax):
        if jump: #logica de animacion del salto
            self.rect.y -= jumpCount
            if self.rect.y > 650:
                jump = False
                jumpMax = 20
                self.rect.y = 660
            elif jumpCount > -jumpMax:
                jumpCount -= 1
            else:
                jump = False
                jumpMax = 20
        
        return (jump, jumpCount, jumpMax)         
        


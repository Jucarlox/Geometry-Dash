import pygame

class Obstaculo:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = "purple"
        self.velocidad = 4
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)
    
        
    def movimiento(self):
        self.x -= self.velocidad
        
        
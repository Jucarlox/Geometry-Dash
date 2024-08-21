import pygame
from personaje import Cubo
from obstaculo import Obstaculo

pygame.init()
run = True
VENTANA = pygame.display.set_mode([1800, 1000])
color_mundo = (0, 0, 64)
suelo = (0, 750, 1800, 100)
color_suelo = (0, 0, 0)
clock = pygame.time.Clock()
cubo = Cubo()
jump = False
jumpCount = 0
jumpMax = 20
FPS = 120

obstaculos = []

tiempo_pasado = 0
tiempo_entre_objetos = 1000


 


while run:
    
    VENTANA.fill(color_mundo)#damos color a la ventana
    clock.tick(FPS) #creamos un delay para que los saltos tengan fluidez
    tiempo_pasado += clock.tick(FPS)
    
    if tiempo_pasado > tiempo_entre_objetos:
        obstaculos.append(Obstaculo(1800,650,100,100))
        tiempo_pasado = 0    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #evento cerrar el juego
            run = False
        if event.type == pygame.KEYDOWN: #evento de salto
            cubo.image = pygame.transform.rotate(cubo.image, -90) #rotamos el personaje al saltar
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                jumpCount = jumpMax
    
    
    salto = cubo.salto(jump, jumpCount, jumpMax)
    jump = salto[0]
    jumpCount = salto[1]

    for obstaculo in obstaculos:
        obstaculo.dibujar(VENTANA)
        obstaculo.movimiento()
        
        if pygame.Rect.colliderect(cubo.rect, obstaculo.rect):
            print(cubo.rect.y)
            print(obstaculo.rect.y)
            if cubo.rect.y+cubo.rect.height < obstaculo.rect.y+obstaculo.rect.height:
                #cubo.rect.y -= obstaculo.rect.height
                jump = False
            else:
                pygame.QUIT
                run = False
        

    pygame.draw.rect(VENTANA, color_suelo, suelo)
    VENTANA.blit(cubo.image, cubo.rect)
    
    #pygame.display.flip()
    pygame.display.update()

pygame.quit()
exit() 
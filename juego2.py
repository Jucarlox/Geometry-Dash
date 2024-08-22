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
tiempo_entre_objetos = 500

colision = False
puntos = 0
 
FUENTE = pygame.font.SysFont("Comic Sans", 40)

while run:
    
    VENTANA.fill(color_mundo)#damos color a la ventana
    clock.tick(FPS) #creamos un delay para que los saltos tengan fluidez
    tiempo_pasado += clock.tick(FPS)
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")
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
    jumpMax = salto[2]
    

    for obstaculo in obstaculos:
        obstaculo.dibujar(VENTANA)
        obstaculo.movimiento()
        
        if pygame.Rect.colliderect(cubo.rect, obstaculo.rect):
            print("si")
            if cubo.rect.y+cubo.rect.height < obstaculo.rect.y+obstaculo.rect.height:
                jump = False
                colision = True
                jumpMax = 20
            else:
                pygame.QUIT
                run = False

        if colision == True and jump == False and (cubo.rect.x > obstaculo.rect.x + obstaculo.rect.width):
            jump = True
            colision = False
            obstaculos.remove(obstaculo)
            puntos += 1
        elif (cubo.rect.x > obstaculo.rect.x + obstaculo.rect.width):
            obstaculos.remove(obstaculo)
            puntos += 1
            colision = False    
        elif colision == True and jump == True and (cubo.rect.x < obstaculo.rect.x + obstaculo.rect.width):
            jumpMax = jumpMax + (jumpMax - jumpCount) + 100
            colision = False
                

    pygame.draw.rect(VENTANA, color_suelo, suelo)
    VENTANA.blit(cubo.image, cubo.rect)
    
    #pygame.display.flip()
    VENTANA.blit(texto_puntos, (20, 20))
    pygame.display.update()

pygame.quit()
exit() 
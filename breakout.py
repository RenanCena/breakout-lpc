import pygame
from sys import exit

pygame.init()

# criando janela
size = (480, 840)
screen = pygame.display.set_mode(size)
# legenda / nome do jogo
pygame.display.set_caption("MyBreakout - PyGame Edition")
clock = pygame.time.Clock()

# imagem de fundo
background = pygame.image.load("graphics/bg.png") 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))
    
    pygame.display.update()
    clock.tick(60)
import pygame
import bird

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")

    #Métodos do pássaro
    bird.Create_Bird(screen)
    bird.Jumping()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
import pygame
import bird
import pipe

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
    bird.Pbird.Create_Bird(screen)
    bird.Pbird.Jumping()
    bird.Pbird.Apply_Gravity()

    #Métodos dos canos
    pipe.Pipes.Create_Pipes(screen)
    pipe.Pipes.Move_Pipes()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
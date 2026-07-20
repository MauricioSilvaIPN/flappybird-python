import pygame
import bird
import pipe

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

score_font = pygame.font.SysFont("Comic Sans MS", 80)
score_number = 0


def UpdateScore():
    global score_number
    new_score = str(score_number)

    text_surface = score_font.render(new_score, False, (0, 0, 0))
    screen.blit(text_surface, (1200, 0))

    if pipe.Pipes.normal_pipe.rect.x < bird.Pbird.bird.rect.x:
        score_number += 1


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("aquamarine")

    #Métodos próprios
    UpdateScore()   

    #Métodos do pássaro
    bird.Pbird.Create_Bird(screen)
    bird.Pbird.Jumping()
    bird.Pbird.Apply_Gravity()
    bird.Pbird.Death()

    #Métodos dos canos
    pipe.Pipes.Move_Pipes()
    pipe.Pipes.Create_Pipes(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
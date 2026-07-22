import pygame
import pipe

draw_group = pygame.sprite.Group()

gravity_power = 5
jump_power = 85


class Pbird:
    vermelho = (255, 0, 0)

    is_dead = False
    can_jump = True
    can_gravity = True
    jump_timer = 1.0


    bird = pygame.sprite.Sprite(draw_group)
    bird.image = pygame.image.load("/home/mauricio/Documentos/Programmer Docs/VSCode Docs/Projetos/FlappyBird-game/game/PyGame-FB Sprites/Pixel art - Pássaro.png")

    bird.image = pygame.transform.scale(bird.image, [50, 50])
    bird.rect = pygame.Rect(50, 50, 50, 50)

    collider = bird.rect

#    bird.image.fill(vermelho)



    def Create_Bird(display):
        draw_group.draw(display)


    def Apply_Gravity():
        if Pbird.can_gravity:
            Pbird.bird.rect.y += gravity_power



    def Jumping():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and Pbird.can_jump:
            Pbird.bird.rect.y -= jump_power   
            Pbird.can_gravity = False
            Pbird.can_jump = False
            

        if Pbird.can_jump == False:
            Pbird.jump_timer -= 0.1
        

        if Pbird.jump_timer <= 0:
            Pbird.can_jump = True
            Pbird.can_gravity = True
            Pbird.jump_timer = 1.0
    

    def BirdDeath():
        if Pbird.collider.colliderect(pipe.Pipes.normal_pipe) or Pbird.collider.colliderect(pipe.Pipes.upside_pipe):
            Pbird.is_dead = True


    def BirdBirth(display):
        Pbird.bird.rect = pygame.Rect(50, 50, 50, 50)

        draw_group.draw(display)


            
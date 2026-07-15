import pygame

draw_group = pygame.sprite.Group()

gravity_power = 5
jump_power = 85

class Pbird:
    can_jump = True
    can_gravity = True
    jump_timer = 1.0


    bird = pygame.sprite.Sprite(draw_group)
    bird.image = pygame.image.load("/home/mauricio/Documentos/Programmer Docs/VSCode Docs/Projetos/FlappyBird-game/game/PyGame-FB Sprites/Pixel art - Pássaro.png")

    bird.image = pygame.transform.scale(bird.image, [100, 100])
    bird.rect = pygame.Rect(50, 50, 100, 100)


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
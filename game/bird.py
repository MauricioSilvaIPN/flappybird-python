import pygame

draw_group = pygame.sprite.Group()

gravity_power = 5
jump_power = 10
can_jump = True


class bird:
    bird = pygame.sprite.Sprite(draw_group)
    bird.image = pygame.image.load("/home/mauricio/Documentos/Programmer Docs/VSCode Docs/Projetos/FlappyBird-game/game/PyGame-FB Sprites/Pixel art - Pássaro.png")

    bird.image = pygame.transform.scale(bird.image, [100, 100])
    bird.rect = pygame.Rect(50, 50, 100, 100)


    def Create_Bird(display):
        draw_group.draw(display)


    def Apply_Gravity():
        bird.bird.rect.y += gravity_power



    def Jumping():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            bird.bird.rect.y -= jump_power                
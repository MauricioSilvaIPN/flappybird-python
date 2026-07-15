import pygame

draw_group = pygame.sprite.Group()

speed_move = 5

class Pipes:
    normal_pipe = pygame.sprite.Sprite(draw_group)
    upside_pipe = pygame.sprite.Sprite(draw_group)

    normal_pipe.image = pygame.image.load("/home/mauricio/Documentos/Programmer Docs/VSCode Docs/Projetos/FlappyBird-game/game/PyGame-FB Sprites/Pixel art - PipeNormal.png")
    upside_pipe.image = pygame.image.load("/home/mauricio/Documentos/Programmer Docs/VSCode Docs/Projetos/FlappyBird-game/game/PyGame-FB Sprites/Pixel art - PipeUpSidel.png")

    normal_pipe.image = pygame.transform.scale(normal_pipe.image, [100, 500])
    upside_pipe.image = pygame.transform.scale(upside_pipe.image, [100, 500])

    normal_pipe.rect = pygame.Rect(1280, 550, 100, 100)
    upside_pipe.rect = pygame.Rect(1280, 0, 100, 100)


    def Create_Pipes(display):
        draw_group.draw(display)

        if Pipes.normal_pipe.rect.x <= 0 and Pipes.upside_pipe.rect.x <= 0:
            #Pipes.normal_pipe.kill()
            #Pipes.upside_pipe.kill()
            Pipes.Spawn_Pipes()


    def Move_Pipes():
        Pipes.normal_pipe.rect.x -= speed_move
        Pipes.upside_pipe.rect.x -= speed_move


    def Spawn_Pipes():
        Pipes.normal_pipe.image = pygame.image.load("/home/mauricio/Documentos/Programmer Docs/VSCode Docs/Projetos/FlappyBird-game/game/PyGame-FB Sprites/Pixel art - PipeNormal.png")
        Pipes.upside_pipe.image = pygame.image.load("/home/mauricio/Documentos/Programmer Docs/VSCode Docs/Projetos/FlappyBird-game/game/PyGame-FB Sprites/Pixel art - PipeUpSidel.png")

        Pipes.normal_pipe.image = pygame.transform.scale(Pipes.normal_pipe.image, [100, 500])
        Pipes.upside_pipe.image = pygame.transform.scale(Pipes.upside_pipe.image, [100, 500])

        Pipes.normal_pipe.rect = pygame.Rect(1280, 550, 100, 100)
        Pipes.upside_pipe.rect = pygame.Rect(1280, 0, 100, 100)
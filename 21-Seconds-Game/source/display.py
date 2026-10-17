import pygame
from button import Button

def start():
    pygame.init()
    (width, height) = (1000, 500)
    screen = pygame.display.set_mode((width, height))
    backgroundColour = [53, 101, 77]

    playImage = pygame.image.load("21-Seconds-Game/assets/Buttons/play-button.png").convert_alpha()
    exitImage = pygame.image.load("21-Seconds-Game/assets/Buttons/exit-button.png").convert_alpha()
    playButton = Button(150, 250, playImage, 6)
    exitButton = Button(550, 250, exitImage, 6)

    pygame.display.flip()

    running = True
    while running:

        screen.fill(backgroundColour)
        playButton.draw(screen)
        exitButton.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
start()

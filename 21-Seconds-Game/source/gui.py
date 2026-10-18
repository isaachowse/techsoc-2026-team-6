import pygame
import sys
from card import Suit, CardType, BaseCard

class GameGUI:
    def __init__(self, width=800, height=600):
        pygame.init()
        info = pygame.display.Info()
        self.width = info.current_w
        self.height = info.current_h
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)

        self.clock = pygame.time.Clock()

        #self.font = pygame.font.SysFont(None, 32)

        # self.hit_button_rect = pygame.Rect(200, 200, 120, 50)

        # self.stand_button_rect = pygame.Rect(200, 200, 120, 50)

        self.hit_image = pygame.image.load("21-Seconds-Game/assets/Buttons/play-button.png").convert_alpha()
        self.stand_image = pygame.image.load("21-Seconds-Game/assets/Buttons/stand-button.png").convert_alpha()

        self.setup_buttons()


    def setup_buttons(self):
        #Get button positions based on screen size
        button_width = 120
        button_height = 50
        gap = 20

        button_group_width = (button_width * 2) + gap
        start_x = (self.width - button_group_width) // 2
        start_y = self.height - button_height - 500

        self.hit_button_rect = pygame.Rect(start_x, start_y, button_width, button_height)
        self.stand_button_rect = pygame.Rect(start_x + button_width + gap, start_y, button_width, button_height)



    def draw_buttons(self):
        # 1. Draw Hit Button (Reddish)
        #pygame.draw.rect(self.screen, (200, 50, 50), self.hit_button_rect, border_radius=8)
        #hit_text = self.font.render("Hit", True, (255, 255, 255))
        self.screen.blit(self.hit_image, self.hit_button_rect.topleft)
        self.screen.blit(self.stand_image, self.stand_button_rect.topleft)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill screen with green to test
            self.screen.fill((23, 105, 0))
            self.draw_buttons()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()



game = GameGUI()
game.run()
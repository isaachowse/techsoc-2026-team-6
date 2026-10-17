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

        self.font = pygame.font.SysFont(None, 32)

        # self.hit_button_rect = pygame.Rect(200, 200, 120, 50)

        # self.stand_button_rect = pygame.Rect(200, 200, 120, 50)

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
        pygame.draw.rect(self.screen, (200, 50, 50), self.hit_button_rect, border_radius=8)
        hit_text = self.font.render("Hit", True, (255, 255, 255))
        self.screen.blit(hit_text, (self.hit_button_rect.x + 45, self.hit_button_rect.y + 12))

        #Draw Stand Button
        pygame.draw.rect(self.screen, (50, 50, 200), self.stand_button_rect, border_radius=8)
        stand_text = self.font.render("Stand", True, (255, 255, 255))
        self.screen.blit(stand_text, (self.stand_button_rect.x + 30, self.stand_button_rect.y + 12))

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
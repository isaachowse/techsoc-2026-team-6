import pygame 
from animations import (move_card, flip_card, button_animation, score_flash_animation, result_animation)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption ("Animation Demo")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
big_font = pygame.font.SysFont(None, 65)

GREEN = (20,100, 60)
WHITE = (255, 255, 255)

hit_button = pygame.Rect (180, 480, 160, 60)
stand_button = pygame. Rect (60, 480, 160, 60)

start_x = 650
start_y = 100

card_x = start_x
card_y =  start_y 

target_x = 300
target_y = 300

card_back = pygame.Surface((80, 120))
card_back.fill((40, 70, 180))

card_front = pygame.Surface((80, 120))
card_front.fill(WHITE)

screen.blit(card_front, (card_x, card_y))

moving = False 
flipping = False 
progress = 0


score = 13
timer = 0 

result = None
result_size = 0 

running = True 

while running:
  clock.tick(60)

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False 
      if event.type == pygame.K_f:
          if event.button == 1:
            mouse_x, mouse_y = event.pos 

            if 180 <= mouse_x <= 340 and 480 <= mouse_y <=540:
              if not moving and not flipping and result is None:
                card_x =  start_x
                card_y = start_y 
                progress = 0
                moving = True

            elif 460 <= mouse_x <= 620 and 480 <= mouse_y <= 540:
              if not moving and not flipping and result is None:
                if score <=21:
                  result = "win"
                else:
                  result = "lose"

                result_size = 0 
      if moving:
        card_x, card_y, done = move_card(card_x, card_y, target_x. target_y)
        if done:
          moving = False
          flipping = True 

      if flipping:
        progress += 1 
        if progress >= 20:
          progress = 20
          flipping = False
          score += 5
          timer = 15
          if score > 21:
            result = "lose"
            result_size = 0
          
        if timer > 0:
          timer -= 1

        if result is not None and result_size < 20:
          result_size +=1


          screen.fill(GREEN)

          card_image = flip_card(card_back, card_front, progress)
          draw_x =  card_x + (80 - card.image.get_width()) / 2 
          screen.blit(card_image, (draw_x, card_y))

          mouse_x, mouse_y = pygame.mouse.get_pos()

          hit_glow = 180 <= mouse_x <=340 and 480 <=540
          stand_glow = 460 <= mouse_x <= 620 and 480 <= mouse_y <= 540 

          button_animation(screen, hit_button, (0,180,0), hit_glow)
          button_animation(screen, stand_button, (200,0,0), stand_glow)

          hit_text = font.render("HIT", True, WHITE)
          stand_text = font.render("STAND", True, WHITE)

          screen.blit(hit_text, hit_text.get_rect(center=hit_button.center))
          screen.blit(stand_text, stand_text.get_rect(center=stand_button.center))

          score_text = score_animation (score, timer, font)
          screen.blit(score_text, (350,50))

          if result is not None:
            text =  result_animation(result, big_font, result_size)
            if text is not None:
              text_rect =  text.get_rect(center=(400, 250))
              screen.blit(text, text_text_rect)

          pygame.display.update()

def loadCardImage(self, card):
        suit = card.suit.name.lower() + "s"
        try:
            int(card.type.value)
            type = f"{int(card.type.value):02d}"
        except ValueError:
            type = card.type.value[0].upper()
        imagePath = f"21-Seconds-Game/assets/Cards/PNG/cards-large/card_{suit}_{type}.png"
        cardImage = pygame.image.load(imagePath).convert_alpha()
        cardImage = pygame.transform.scale(cardImage, (int(cardImage.get_width())*2, int(cardImage.get_height())*2))
        return cardImage

pygame.quit()












































    

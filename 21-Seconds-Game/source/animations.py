import pygame 

def move_card (x, y, target_x, target_y, speed=5):
    if x < target_x:
          x = min(x + speed, target_x)

    elif x > target_x:
          x = max(x-speed, target_x)


    if y < target_y:
          y = min(y + speed, target_y)

    elif y > target_y:
          y = max(y - speed, target_y)

    done = (x == target_x and y == target_y)

    return x, y, done 



def flip_card (card_back, card_front, progress):
    progress = max (0, min(progress,1))

    width = card_back.get_width()
    height = card_back. get_height()

    if progress < 0.5:
        new_width = int(width * (1 - progress*2))
        image = card_back

    else:
        new_width = int(width * ((progress - 0.5)*2))
        image = card_front 

    new_width = max(1, new_width)

    flipped_card = pygame.transform.scale(image, (new_width, height))


def button_animation (screen, button, colour, glowing):

    if glowing:
        glow = button. inflate(15, 15)
        pygame.draw.rect(screen, colour, glow, border_radius=12)

    pygame.draw.react(screen, colour, glow, border_radius=10)


def score_flash_animation (score, timer, font):

    if timer > 0:
        colour = (255,255, 0)
    else:
        colour = (255, 255, 255)

    text = font.render(str(score), True, colour)

    return text 


def result_animation(result, font, size):

    if result == "win":
        message = "YOU WON !!!"
        colour = (0, 255, 0)
        
    elif result == "lose":
        message = "you lost, mb :("
        colour = (255, 0, 0)
        
    else: 
        return None 

    text = font.render(message, True, colour)

    width = int(text.get_width() * size / 20)
    height = int(text.get_height() * size / 20)
        
    width = max(1, width)
    height = max(1, height)

    text = pygame.transform.scale(text, (width, height))
    
    return text 
    

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

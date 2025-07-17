import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# RGB Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
brown = (153, 76, 0)
grass_green = (76, 153, 0)
light_gray = (160, 160, 160)
dark_gray = (128, 128, 128)


# snake features
square_size = 20
game_speed = 15


def draw_snake(size, snake_body):
    for snake_part in snake_body:
        if snake_body.index(snake_part) == 0: # snake's head
            pygame.draw.rect(screen, black, [snake_part[0], snake_part[1], size, size])
        elif snake_body.index(snake_part) % 2 != 0:
            pygame.draw.rect(screen, yellow, [snake_part[0], snake_part[1], size, size])
        else:
            pygame.draw.rect(screen, red, [snake_part[0], snake_part[1], size, size])


def generate_food():
    food_x = round(random.randrange(0, screen_width - square_size) / float(square_size)) * float(square_size)
    food_y = round(random.randrange(0, screen_height - square_size) / float(square_size)) * float(square_size)
    return food_x, food_y


def draw_food(size, x, y):
    pygame.draw.rect(screen, red, [x, y, size, size])


def is_opposite_direction(current_x, current_y, new_x, new_y):
    # Checks if player is trying to move the snake to an opposite direction
    return (current_x == -new_x and current_y == new_y) or (current_y == -new_y and current_x == new_x)


def select_speed(key, current_speed_x, current_speed_y):
    new_speed_x, new_speed_y = current_speed_x, current_speed_y
    if key == pygame.K_DOWN:
        if not is_opposite_direction(current_speed_x, current_speed_y, 0, square_size):
            new_speed_x, new_speed_y = 0, square_size
    elif key == pygame.K_UP:
        if not is_opposite_direction(current_speed_x, current_speed_y, 0, -square_size):
            new_speed_x, new_speed_y = 0, -square_size
    elif key == pygame.K_LEFT:
        if not is_opposite_direction(current_speed_x, current_speed_y, -square_size, 0):
            new_speed_x, new_speed_y = -square_size, 0
    elif key == pygame.K_RIGHT:
        if not is_opposite_direction(current_speed_x, current_speed_y, square_size, 0):
            new_speed_x, new_speed_y = square_size, 0
    return new_speed_x, new_speed_y


def show_score(score):
    font = pygame.font.SysFont("Helvetica", 40)
    text = font.render(f"Score: {score}", True, black)
    screen.blit(text, [1, 1])


def play_game():
    game_over = False

    # starting position
    x = screen_width // 2
    y = screen_height // 2

    # starting move speed
    speed_x = square_size # snake starts moving to the right
    speed_y = 0

    # snake_size
    snake_size = 1
    snake_body = []

    food_x, food_y = generate_food()

    while not game_over:
        screen.fill(grass_green)

        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key, speed_x, speed_y)

        # Draw Food
        draw_food(square_size, food_x, food_y)

        # Update Snake's position
        x += speed_x
        y += speed_y

        # Draw Snake
        snake_body.insert(0, [x, y])
        if len(snake_body) > snake_size:
            snake_body.pop()
        
        # Check if snake hits it's own body
        for snake_part in snake_body[1:]:
            if snake_part == [x, y]:
                game_over = True

        # Check if snake hits the screen borders
        if (x < 0) or (x >= screen_width) or (y < 0) or (y >= screen_height):
            game_over = True

        draw_snake(square_size, snake_body)
        show_score(snake_size - 1)

        # Update Screen
        pygame.display.update()

        # Generate new food
        if (x == food_x) and (y == food_y):
            snake_size += 1
            food_x, food_y = generate_food()

        clock.tick(game_speed)



play_game()
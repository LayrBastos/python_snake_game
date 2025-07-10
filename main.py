import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")
screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# RGB Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# snake features
square_size = 20
game_speed = 15


def generate_food():
    food_x = round(random.randrange(0, screen_width - square_size) / float(square_size)) * float(square_size)
    food_y = round(random.randrange(0, screen_height - square_size) / float(square_size)) * float(square_size)
    return food_x, food_y

def draw_food(size, x, y):
    pygame.draw.rect(screen, red, [x, y, size, size])

def play_game():
    game_over = False

    # starting position
    x = screen_width // 2
    y = screen_height // 2

    # starting move speed
    speed_x = 0
    speed_y = 0

    # snake_size
    snake_size = 1
    snake_body = []

    food_x, food_y = generate_food()

    while not game_over:
        screen.fill(black)

        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                game_over = True

        draw_food(square_size, food_x, food_y)

        snake_body.append(x, y)


        pygame.display.update()
        clock.tick(game_speed)



play_game()
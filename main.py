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


def draw_snake(size, snake_body):
    for snake_part in snake_body:
        pygame.draw.rect(screen, white, [snake_part[0], snake_part[1], size, size])


def generate_food():
    food_x = round(random.randrange(0, screen_width - square_size) / float(square_size)) * float(square_size)
    food_y = round(random.randrange(0, screen_height - square_size) / float(square_size)) * float(square_size)
    return food_x, food_y


def draw_food(size, x, y):
    pygame.draw.rect(screen, red, [x, y, size, size])


def select_speed(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = square_size
    elif key == pygame.K_UP:
        speed_x = 0
        speed_y = -square_size
    elif key == pygame.K_LEFT:
        speed_x = -square_size
        speed_y = 0
    elif key == pygame.K_RIGHT:
        speed_x = square_size
        speed_y = 0   
    return speed_x, speed_y


def show_score(score):
    font = pygame.font.SysFont("Helvetica", 40)
    text = font.render(f"Score: {score}", True, green)
    screen.blit(text, [1, 1])


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
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)

        # Draw Food
        draw_food(square_size, food_x, food_y)

        # Update Snake's position
        x += speed_x
        y += speed_y

        # Draw Snake
        snake_body.append([x, y])
        if len(snake_body) > snake_size:
            del snake_body[0]
        
        # Check if snake hits it's own body
        for snake_part in snake_body[:-1]:
            if snake_part == [x, y]:
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
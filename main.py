import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")
screen_width, screen_height = 600, 400
pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# RGB Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# snake features
square_size = 10
snake_speed = 15

def play_game():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                game_over = True





play_game()
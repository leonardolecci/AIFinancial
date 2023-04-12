import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pinball")

# Set up game variables
ball_pos = [300, 400]
ball_radius = 10
ball_speed = [random.randint(-5, 5), random.randint(-5, 5)]

# Set up the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Draw the game objects
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()

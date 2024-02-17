# Example file showing a basic pygame "game loop"
import dt
import pygame
import random

from xlrd.formatting import x

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def generate_starting_position():
    position_range = (pixel_width // 2, pixel_width)
    return [random.randrange(*range), random.randrange(*range)]

#playground
pixel_width = 50

#snake
snake_pixel = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
snake = [snake_pixel.copy()]

#target
target = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
target.center = generate_starting_position()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos:y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos:y += 300 * dt
    if keys[pygame.K_a]:
        player_pos:x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos:x += 300 * dt

    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)

    pygame.draw.rect(screen, "red", target)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

import pygame
import random
import time

class Player(pygame.sprite.Sprite):
    #Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(cyan)
        self.rect = self.image.get_rect()
        self.rect.center = (360/2,480/2) 

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
cyan = (0,255,255)
purple = (255,0,255)
colour = [white ,black,red,green,cyan,purple]



# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#A group of sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    for c in colour:
        screen.fill(c)
        time.sleep(0.5)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()

import pygame
import random
import time
import os
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    #Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "/home/ayush/Documents/Game/p1_jump.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (360/2,480/2) 
        self.y_speed = 1
   
    def update(self):
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT-150:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        self.rect.x +=5
        if self.rect.left >= WIDTH:
            self.rect.right = 0
    
WIDTH = 800
HEIGHT = 600
FPS = 45

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
    screen.fill(cyan)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()


pygame.quit()

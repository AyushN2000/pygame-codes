import pygame 
import random
import time
#pygame initializations
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((480,480))
clock = pygame.time.Clock()

#colour rgb values
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
cyan = (0,255,255)
purple = (255,0,255)
colour = [white ,black,red,green,cyan,purple]


#Game loop
running = True
while running:
    
    #Keeps the game to maintain a particular frame rate
    clock.tick(30)
    
    #Checks for aterminating condition , or can take any input from user and used so.
    for event in pygame.event.get():
        
        #Terminates window if the 'X' sign is pressed
        if event.type == pygame.QUIT:
            running = False
    
    #fills colours into screen
    for c in colour:
        screen.fill(c)
        time.sleep(0.5)
        pygame.display.flip()

pygame.quit()
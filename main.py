import pygame
from time import perf_counter
from pygame.locals import (
    QUIT,
    KEYDOWN,
    KEYUP,
    K_w,
    K_s,
    K_d,
    K_a
)
pygame.init()


#Window Stuff
FPS = 120
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
WINDOW_SIZE = (900, 600) #x, y
pygame.display.set_caption("Template") 
#Set the Caption Window Like 'Terraria: Also Try Minecraft'
DISPLAY = pygame.display.set_mode(WINDOW_SIZE, 0, 32) #True Screen
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) #Screen to Blit on other Screen
HDMode = True


def Game():
    last_dt = perf_counter()
    program_running = True
    while program_running:
        dt = (perf_counter() - last_dt)*FPS
        last_dt = perf_counter()
        for event in pygame.event.get():
            if event.type == KEYDOWN: #if a key is pressed down
                pass

            elif event.type == KEYUP: # if a key is pressed up
                pass

            elif event.type == QUIT:
                program_running = False
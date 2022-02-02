
import pygame
from statistics import mean
from Player import PlayerObject
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
pygame.display.init()
print ('test')
#
#Window Stuff
FPS = 120 #<show> Base Frames Per Second of the Game
SCREEN_WIDTH = 1920 #<show> pixel Width of the game
SCREEN_HEIGHT = 1080 #<show> pixel height of the game
WINDOW_SIZE = (960, 540) #x, y
pygame.display.set_caption("Template") #<show> Sets the caption of pygame window
#Set the Caption Window Like 'Terraria: Also Try Minecraft'
DISPLAY = pygame.display.set_mode(WINDOW_SIZE, 0, 32) #True Screen
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) #Screen to Blit on other Screen
HDMode = True #<show> whether  

P1 = PlayerObject((K_w, K_s, K_d, K_a))#<show> Object of Player 1
def Game(): #<show> Call Function of the game
    displayframe=[]
    PLAYERS = [P1] #<show> Holds the List of Players
    last_dt = perf_counter() #<show> last Game Loop time
    program_running = True #<show> Boolean thattells if the game is running or not
    while program_running: #<show> While Game is running
        dt = (perf_counter() - last_dt)*FPS #<show> calculate the movement multiplier for it to be time dependent
        last_dt = perf_counter() #<show> last Game Loop time

        for event in pygame.event.get(): #<show> for new events happening
            #Start Code Block (can be simplified)
            if event.type == KEYDOWN: #if a key is pressed down
                for player in PLAYERS: #<show> for all players in PLAYERS
                    for direction, key in zip(player.movements, player.keys): #<show> get all directions (UP, DOWN, LEFT, RIGHT)
                        if event.key == key: #<show> if new event is player control key
                            player.movements[direction] = True #<show> set direction to True
            elif event.type == KEYUP: # if a key is pressed up
                for player in PLAYERS: #<show> for all players in PLAYERS
                    for direction, key in zip(player.movements, player.keys): #<show> get all directions (UP, DOWN, LEFT, RIGHT)
                        if event.key == key: #<show> if new event is player control key
                            player.movements[direction] = False #<show> set direction to True
            #End Code Block
            elif event.type == QUIT: #<show> if new event is quit
                program_running = False #<show> set the game loop off
        
        #GAME LOGIC
        for player in PLAYERS: #<show> for every player
            player.update(dt) #<show> update player
        
        #DRAWING
        SCREEN.fill((14, 18, 36)) #<show> fill the screen with the background colour
        for player in PLAYERS: #<show> for every player
            SCREEN.blit(player.image, (player.x, player.y)) #<show> Paste the player image at the player coordinate on the SCREEN
        
        #SCREEN
        if HDMode: #<show> if High Definition Mode is True
            DISPLAY.blit(pygame.transform.smoothscale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by scaling it to it's resolution 
        else: #<show> if high Definition Mode is False
            DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by smooth scaling it to it's resolution 
        pygame.display.update() #<show> Update the Screen
        displayframe.append(1/(perf_counter()-last_dt))
    print ('')
    print (mean(displayframe[10:]))
Game()
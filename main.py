from random import randint, choice, random
from Bullets import BulletObject
from MenuObjects import ButtonObject, ScreenObject
from Trails import TrailObject
from enginePure import EMPTY_COLOR, FULL_COLOR, WHITE, CameraObject, ColorOverview, DynamicColor, LinearPoint, PolygonClass, PolygonOverview, StaticColor, StaticPoint, convertPointToMid, regularShape, verticesForCircle, RGBtoStaticColor, RAINBOW
from math import degrees, atan2
from enginePure import Overview
import pygame
from statistics import mean
from Player import PlayerObject
from Level import LEVEL0, LEVEL1, LEVEL2, LEVEL3
from time import perf_counter, sleep
from pygame.locals import (
    QUIT,
    KEYDOWN,
    KEYUP,
    K_w,
    K_s,
    K_d,
    K_a,
    K_SPACE,
    K_ESCAPE,
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
)


class LevelRunner(object):
    def __init__(self, level, Music=None):
        # <show> converts the script into eval funcs
        self.level = self.convertScriptToEvalFunc(level)
        # <show> holds the current index it is through the list.
        self.index = 0
        self.isMusic = False  # <show> music is true
        if self.isMusic:  # <show> if there is Music
            pygame.mixer.init()  # <show> initialise pygame.mixer
            # <show> holds the ending sound for the level.
            self.ENDINGMUSIC = pygame.mixer.Sound('data/Music/EndingSound.wav')
            # <show> set the ending level sound to a certain percent
            self.ENDINGMUSIC.set_volume(0.05)
            if Music is not None:  # <show> if there is a song for the level
                # <show> store the song as an attribute
                self.MUSIC = pygame.mixer.Sound(f'data/Music/{Music}')
                # <show> set the volume of the music
                self.MUSIC.set_volume(0.05)
                self.MUSIC.play(-1)  # <show> play the music indefinetly.
            else:
                self.MUSIC = None  # <show> set Music as none
        self.start = perf_counter()  # <show> holds when the levelRunner was created
        self.Trin = None  # <show> if Trin is true which is the ending triangle which ends the level
        self.finish = None  # <show> if the game is finished

    def update(self):  # <show> when updating
        self.spawning()  # <show> run the bullet spawning function
        # <show> if Trin has spawned but hasn't collided.
        if self.Trin is not None and self.finish is None:
            for player in Overview.PLAYERS:  # <show> for all players in the game
                if self.Trin.get_rect().colliderect(player.get_rect()):  # <show> if any player collides with the
                    Overview.GLOBALFADE.fadeTo(WHITE, 1.6)
                    # <show> turn every player invincible
                    [i.turnInvincible(5) for i in Overview.PLAYERS]
                    if self.isMusic:  # <show> if Music is allowed
                        self.ENDINGMUSIC.play()  # <show> play the ending music
                        if self.MUSIC:  # <show> if there is Background Music
                            # <show> fade out the background music
                            self.MUSIC.fadeout(1000)
                    self.finish = perf_counter()  # <show> set the current time as self.finish
                    break
        # <show> if it has been over 1.6 seconds since the collision
        if self.finish is not None and 1.6 < perf_counter() - self.finish:
            Overview.GLOBALFADE.fadeFrom(
                WHITE, 1000000)  # <show> fade to white
            return True  # <show> return True meaning that the level has ended
        return False  # <show> otherwise return false

    def spawning(self):
        # <show> if the current index is still going through the script the current index time is less than the current time elapsed.
        while self.index < len(self.level) and self.level[self.index][0] < perf_counter() - self.start:
            # <show> run the function that came with it
            self.level[self.index][1]()
            self.index += 1  # <show> increase the index

    def convertScriptToEvalFunc(self, level):
        # <show> converts the string to code via lambda, basically precompiling the code
        return tuple([(time, eval('lambda: ' + expression)) for time, expression in level])

    def loop(self):
        self.start = perf_counter()  # <show> set current time as the beginning
        self.index = -1  # <show> set the index as self.index as 0

    def Finish(self, *args):
        if self.Trin is None:
            self.Trin = TrailObject(
                LinearPoint(*args),
                PolygonOverview((PolygonClass(regularShape(40, verticesForCircle(40)), ColorOverview(
                    r=DynamicColor(
                                0, 128, 255, DynamicColor.posSinColor),
                    g=DynamicColor(
                        120, 128, 255, DynamicColor.posSinColor),
                    b=DynamicColor(240, 128, 255, DynamicColor.posSinColor), isGlobal=True)), PolygonClass(regularShape(38, verticesForCircle(38)), ColorOverview(alpha=EMPTY_COLOR, isGlobal=True)), PolygonClass(regularShape(30, 3), ColorOverview(**RGBtoStaticColor(r=211, g=239, b=246), isGlobal=True)), PolygonClass(regularShape(10, 3), ColorOverview(alpha=EMPTY_COLOR, isGlobal=True)),), rotationIncrease=1),
                1000000000)


SCREEN_WIDTH = 1920  # <show> pixel Width of the game
SCREEN_HEIGHT = 1080  # <show> pixel height of the game
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_SIZE = (1280, 720)  # x, y
SCREENTODISPLAYSCALAR = tuple(
    win/scr for win, scr in zip(WINDOW_SIZE, SCREEN_SIZE))
DISPLAYTOSCREENSCALAR = tuple(
    scr/win for win, scr in zip(WINDOW_SIZE, SCREEN_SIZE))


def transformMousePos(mousePos):
    return (mousePos[0]*DISPLAYTOSCREENSCALAR[0],
            mousePos[1]*DISPLAYTOSCREENSCALAR[1],)


# Window Stuff
# chad = BulletObject(
#     LinearPoint(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT), 30, 0.1),
#     PolygonOverview((PolygonClass(regularShape(120, 3), ColorOverview()), PolygonClass(regularShape(60, 3), ColorOverview(alpha=StaticColor(0))), PolygonClass(regularShape(20, 4), ColorOverview(r=FULL_COLOR, g=EMPTY_COLOR, b=EMPTY_COLOR), rotationSpeed=-1)), rotationIncrease=1),
#     1000000000)
# Overview.BULLETS = [chad]
# test = \
# BulletObject(
#     LinearPoint(920, 140, 180, 0),
#     PolygonOverview(
#         (
#             PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
#             PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
#             PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
#             ),
#         rotation=0,
#         rotationIncrease=1
#     ),
#     200)
# test.starting()
# white = ColorOverview()
# test.polygon.fadeFrom(white, duration=1)


LEVELS = ((LEVEL0, None), (LEVEL1, 'CorruptedPart1.wav'),
          (LEVEL2, 'CorruptedPart2.wav'),)
# LEVELS = ((LEVEL3, 'CorruptedPart3.wav'),)


def Game(level, Music):  # <show> Call Function of the game
    GameStart = perf_counter()
    Overview.clean()
    global LEVEL
    framerates = []
    Overview.BGCOLOR = ColorOverview(
        **RGBtoStaticColor(r=8, g=12, b=14), isGlobal=True, starting=True)

    for level, Music in LEVELS:
        Overview.quickClean()
        LEVEL = None
        # <show> Object of Player 1
        P1 = PlayerObject((K_w, K_s, K_a, K_d, K_SPACE))
        #14, 18, 36
        last_dt = perf_counter()
        program_running = True  # <show> Boolean that tells if the menu is running or not
        # <show> Object of Player 1
        #P2 = PlayerObject((K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE))
        Overview.PLAYERS = [P1]  # <show> Holds the List of Players
        Overview.GLOBALFADE.fadeFrom(WHITE, 1)
        program_running = True
        while program_running:  # <show> While Game is running
            # <show> calculate the movement multiplier for it to be time dependent
            dt = (perf_counter() - last_dt)*FPS
            last_dt = perf_counter()  # <show> last Game Loop time
            Overview.TIMEDELAY = 0
            for event in pygame.event.get():  # <show> for new events happening
                # Start Code Block (can be simplified)
                if event.type == KEYDOWN:  # if a key is pressed down
                    if event.key == K_ESCAPE:  # <show> if new event is quit
                        program_running = False
                    for player in Overview.PLAYERS:  # <show> for all players in PLAYERS
                        # <show> get all directions (UP, DOWN, LEFT, RIGHT)
                        for direction, key in zip(player.movements, player.keys):
                            if event.key == key:  # <show> if new event is player control key
                                # <show> set direction to True
                                player.movements[direction] = True
                elif event.type == KEYUP:  # if a key is pressed up
                    for player in Overview.PLAYERS:  # <show> for all players in PLAYERS
                        # <show> get all directions (UP, DOWN, LEFT, RIGHT)
                        for direction, key in zip(player.movements, player.keys):
                            if event.key == key:  # <show> if new event is player control key
                                # <show> set direction to True
                                player.movements[direction] = False
                # End Code Block
                elif event.type == QUIT:  # <show> if new event is quit
                    program_running = False  # <show> set the game loop off

            # GAME LOGIC

            if LEVEL is None:
                if 0 < perf_counter() - GameStart:
                    LEVEL = LevelRunner(level, Music)
            else:
                if program_running:
                    program_running = not LEVEL.update()

            for player in Overview.PLAYERS:  # <show> for every player
                player.update(dt)  # <show> update Player
            for bullet in Overview.BULLETS:  # <show> for every bullet
                bullet.update(dt)  # <show> update bullet
            for trail in Overview.TRAILS:  # <show> for every trail
                trail.update(dt)  # <show> update trail
            Overview.Camera.update(dt)

            # DRAWING
            # <show> fill the screen with the background colour
            SCREEN.fill(Overview.BGCOLOR.giveColorArgs())

            for trail in Overview.TRAILS:  # <show> for every Trail
                # <show> Paste the trail image at the trail coordinate on the SCREEN
                SCREEN.blit(
                    trail.image, Overview.Camera.CameraOffset(
                        trail.x, trail.y))

            for bullet in Overview.BULLETS:  # <show> for every Bullet
                # <show> Paste the bullet image at the bullet coordinate on the SCREEN
                SCREEN.blit(bullet.image, Overview.Camera.CameraOffset(
                    bullet.x, bullet.y))

            for player in Overview.PLAYERS:  # <show> for every Player
                # <show> Paste the player image at the player coordinate on the SCREEN
                SCREEN.blit(player.image, Overview.Camera.CameraOffset(
                    player.x, player.y))

            if HDMode:  # <show> if High Definition Mode is True
                # <show> Display Screen on the Window by scaling it to it's resolution
                DISPLAY.blit(pygame.transform.smoothscale(
                    SCREEN, WINDOW_SIZE), (0, 0))
            else:  # <show> if high Definition Mode is False
                # <show> Display Screen on the Window by smooth scaling it to it's resolution
                DISPLAY.blit(pygame.transform.scale(
                    SCREEN, WINDOW_SIZE), (0, 0))
            pygame.display.update()  # <show> Update the Screen
            framerates.append(1/(perf_counter()-last_dt))
    print('')
    print(f'''
Frames: {mean(framerates[10:])}
Sprites: {len(Overview.PLAYERS+Overview.BULLETS+Overview.TRAILS)}''')


def MainMenu():
    framerates = []
    Overview.clean()
    if Music:
        pygame.mixer.init()
        MUSIC = pygame.mixer.Sound(f'data/Music/MenuMusic.wav')
        MUSIC.set_volume(0.05)
        MUSIC.play(-1)

    last_dt = perf_counter()
    program_running = True  # <show> Boolean that tells if the menu is running or not
    ButtonObject(
        StaticPoint(1166, 259),
        PolygonOverview(
            (
                PolygonClass(((0, 124), (754, 124), (754, 0), (59, 0)), ColorOverview(
                    **RGBtoStaticColor(r=0, g=0, b=0)), rotationSpeed=1, isRotating=False),
            ),
            rotation=0,
            rotationIncrease=0
        ), Game, ColorOverview(
            r=DynamicColor(0, 26, 252, DynamicColor.sinColor),
            g=DynamicColor(0, 205, 35, DynamicColor.sinColor),
            b=DynamicColor(0, 232, 114, DynamicColor.sinColor),
        ), Overview.NEXA_BOLD, 86, 'Start', ColorOverview(**RGBtoStaticColor(r=255, g=255, b=255)), (128, 28))
    ButtonObject(
        StaticPoint(1132, 259),
        PolygonOverview(
            (
                PolygonClass(((0, 124), (23, 124), (79, 0), (58, 0)), ColorOverview(
                    r=DynamicColor(0, 26, 252, DynamicColor.sinColor),
                    g=DynamicColor(0, 205, 35, DynamicColor.sinColor),
                    b=DynamicColor(0, 232, 114, DynamicColor.sinColor),
                ), rotationSpeed=1, isRotating=False),),
            rotation=0,
            rotationIncrease=0
        ), Game, ColorOverview())

    ButtonObject(
        StaticPoint(1317, 433),
        PolygonOverview(
            (
                PolygonClass(((0, 94), (754, 94), (754, 0), (44, 0)), ColorOverview(
                    **RGBtoStaticColor(r=0, g=0, b=0)), rotationSpeed=1, isRotating=False),
            ),
            rotation=0,
            rotationIncrease=0
        ), None, ColorOverview(**RGBtoStaticColor(r=4, g=83, b=87)), Overview.NEXA_BOLD, 64, 'Leave', ColorOverview(**RGBtoStaticColor(r=255, g=255, b=255)), (128, 20))

    ButtonObject(
        StaticPoint(1292, 433),
        PolygonOverview(
            (
                PolygonClass(((0, 94), (16, 94), (60, 0), (44, 0)), ColorOverview(**RGBtoStaticColor(r=4, g=83, b=87)), rotationSpeed=1, isRotating=False),),
            rotation=0,
            rotationIncrease=0
        ), None, ColorOverview())

    polygonTimer = perf_counter()  # <show> current time that squares are created
    # <show> Create BackGround Colour
    Overview.BGCOLOR = ColorOverview(**RGBtoStaticColor(r=13, g=21, b=24))
    shake = perf_counter()  # <show> current time when square is created.
    while program_running:  # <show> While Menu is running
        # <show> calculate the movement multiplier for it to be time dependent
        dt = (perf_counter() - last_dt)*FPS
        last_dt = perf_counter()  # <show> last Game Loop time

        mousePos = transformMousePos(
            pygame.mouse.get_pos())  # <show> get mouse pos
        for event in pygame.event.get():  # <show> for new events happening
            if event.type == pygame.MOUSEBUTTONDOWN:  # <show> if the button is pressing down
                if event.button == 1:  # <show> if it's left click
                    if currentButton is not None:  # <show>
                        function = currentButton.function  # <show> get the function
                        # issue if
                        program_running = False  # <show> return
            elif event.type == KEYDOWN:  # if a key is pressed down
                if event.key == K_ESCAPE:  # <show> if new event is quit
                    program_running = False  # <show> program sto running
            elif event.type == QUIT:  # <show> if new event is quit
                return None
                program_running = False  # <show> set the game loop off
        # LOGIC
        generator = iter(Overview.BUTTONS)
        currentButton = None
        Overview.Camera.update(dt)  # <show> update Camera
        for button in generator:  # <show> for every button
            side = next(generator)  # <show> get the side button
            # <show> if the mouse is touching either of them
            if any((button.underneathMouse(mousePos), side.underneathMouse(mousePos))):
                # <show> turn to secondary Colour
                button.polygon.fadeFrom(button.fadeColor, 0.5)
                side.polygon.fadeFrom(side.fadeColor, 0.5)
                button.font = Overview.NEXA_BOLD
                currentButton = button
            else:
                button.font = Overview.NEXA_LIGHT

        if 1 < perf_counter() - polygonTimer:  # <show> if it is time to create Polygon
            polygonTimer = perf_counter()
            TrailObject(LinearPoint(randint(0, 1920), 1080, 270, 1),  # <show> create a square
                        PolygonOverview((PolygonClass(regularShape(randint(10, 300), 4), color=ColorOverview(
                            r=DynamicColor(
                                0, 128, 255, DynamicColor.posSinColor),
                            g=DynamicColor(
                                120, 128, 255, DynamicColor.posSinColor),
                            b=DynamicColor(
                                240, 128, 255, DynamicColor.posSinColor),
                            alpha=StaticColor(80), isGlobal=True), rotationSpeed=random()*choice((-1, 1))),), randint(1, 360), 1, starting=True), 14)

        if 0.46875 < perf_counter() - shake:  # <show> if it is time for shake
            shake = perf_counter()
            Overview.Camera.Blinking(0.2, y=5)  # <show> Screen shake
            Overview.BGCOLOR.fade.fadeFrom(WHITE, 0.2, 0.05)
        for button in Overview.BUTTONS:  # <show> for all buttons
            button.update(dt)  # <show> update button
        for trail in Overview.TRAILS:  # <show> for all trail in Trails
            trail.update(dt)  # <show> update trail
        # Drawing
        # <show> fill Screen with background colour
        SCREEN.fill(Overview.BGCOLOR.giveColorArgs())
        for trail in Overview.TRAILS:
            SCREEN.blit(
                trail.image, Overview.Camera.CameraOffset(trail.x, trail.y))

        for button in Overview.BUTTONS:
            SCREEN.blit(button.image, Overview.Camera.CameraOffset(
                button.x, button.y))

        if HDMode:  # <show> if High Definition Mode is True
            # <show> Display Screen on the Window by scaling it to it's resolution
            DISPLAY.blit(pygame.transform.smoothscale(
                SCREEN, WINDOW_SIZE), (0, 0))
        else:  # <show> if high Definition Mode is False
            # <show> Display Screen on the Window by smooth scaling it to it's resolution
            DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0))
        pygame.display.update()  # <show> Update the Screen
        framerates.append(1/(perf_counter()-last_dt))
    if Music:
        MUSIC.fadeout(1000)
    print('')
    print(f'''
Frames: {mean(framerates[10:])}''')
    return 1


# def Template():
#     framerates=[]
#     program_running = True #<show> Boolean that tells if the menu is running or not
#     while program_running: #<show> While Menu is running
#         dt = (perf_counter() - last_dt)*FPS #<show> calculate the movement multiplier for it to be time dependent
#         last_dt = perf_counter() #<show> last Game Loop time


#         for event in pygame.event.get(): #<show> for new events happening
#             if event.type == QUIT: #<show> if new event is quit
#                 program_running = False #<show> set the game loop off
#         #LOGIC

#         #Drawing
#         if HDMode: #<show> if High Definition Mode is True
#             DISPLAY.blit(pygame.transform.smoothscale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by scaling it to it's resolution
#         else: #<show> if high Definition Mode is False
#             DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by smooth scaling it to it's resolution
#         pygame.display.update() #<show> Update the Screen
#         framerates.append(1/(perf_counter()-last_dt))
#     print ('')
#     print (f'''
# Frames: {mean(framerates[10:])}''')


if __name__ == '__main__':
    pygame.display.init()
    pygame.font.init()
    print([i for i in pygame.display.list_modes() if i[0]/16 == i[1]/9])
    FPS = 120  # <show> Base Frames Per Second of the Game

    # <show> Sets the caption of pygame window
    pygame.display.set_caption("Template")
    # Set the Caption Window Like 'Terraria: Also Try Minecraft'
    DISPLAY = pygame.display.set_mode(WINDOW_SIZE)  # True Screen
    # DISPLAY = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN) #True Screen
    # Screen to Blit on other Screen
    SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    HDMode = True  # <show> whether the game runs on high definition meaning higher quality
    Music = True

    if MainMenu() == 1:
        Game(LEVEL1, 'CorruptedPart1.wav')
        # Game (LEVEL0, None)
    pygame.display.quit()

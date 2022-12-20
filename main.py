import pygame
from random import randint, choice, random
from data.EngineAndSprites.MenuObjects import ButtonObject
from data.EngineAndSprites.Trails import TrailObject
from data.EngineAndSprites.Bullets import BulletObject
from data.EngineAndSprites.enginePure import EMPTY_COLOR, WHITE, ColorOverview, DecayingNumber, DynamicColor, LinearPoint, PolygonClass, PolygonOverview, StaticColor, StaticPoint, convertPointToMid, regularShape, verticesForCircle, RGBtoStaticColor, createBox
from data.EngineAndSprites.enginePure import Overview
from statistics import mean
from data.EngineAndSprites.Player import PlayerObject
from data.EngineAndSprites.Level import LEVEL0, LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5, LEVEL6, LEVEL7
from time import perf_counter
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
    def __init__(self, level, Music=None, GLOBALSOUND=False):
        # <show> converts the script into eval funcs
        self.level = self.convertScriptToEvalFunc(level)
        # <show> holds the current index it is through the list.
        self.index = 0
        self.isMusic = GLOBALSOUND  # <show> music is true
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
                self.MUSIC.play(-1)  # <shd ow> play the music indefinetly.
            else:
                self.MUSIC = None  # <show> set Music as none
        
        self.start = perf_counter()  # <show> holds when the levelRunner was created
        self.Trin = None  # <show> if Trin is true which is the ending triangle which ends the level
        self.finish = None  # <show> if the game is finished

    def update(self):  # <show> when updating
        self.spawning()  # <show> run the bullet spawning function
        # <show> if it has been over 1.6 seconds since the collision
        if self.finish is not None:
            if 1.6 < perf_counter() - self.finish:
                Overview.GLOBALFADE.fadeFrom(
                    WHITE, 1000000)  # <show> fade to white
                return True  # <show> return True meaning that the level has ended
            else:
                self.speed.update()
                self.Trin.polygon.internalRotationIncrease = 11 - self.speed.currentNumber
                self.Trin.polygon.internalRotationIncrease = 11 - self.speed.currentNumber
        # <show> if Trin has spawned but hasn't collided.
        elif self.Trin is not None:
            for player in Overview.PLAYERS:  # <show> for all players in the game
                if self.Trin.get_rect(0.2).colliderect(player.get_rect()):  # <show> if any player collides with the Trin
                    Overview.GLOBALFADE.fadeTo(WHITE, 1.6)
                    # <show> turn every player invincible
                    for i in Overview.PLAYERS:
                        i.turnInvincible(5)
                        i.isMoving = False
                        i.x, i.y = self.Trin.x, self.Trin.y
                    if self.isMusic:  # <show> if Music is allowed
                        self.ENDINGMUSIC.play()  # <show> play the ending music
                        self.stopSongs(1000)
                    self.finish = perf_counter()  # <show> set the current time as self.finish
                    self.speed = DecayingNumber()
                    self.speed.setDecayingValue(10, 1.6)
                    break
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
                    b=DynamicColor(240, 128, 255, DynamicColor.posSinColor), isGlobal=True)), 
                    PolygonClass(regularShape(38, verticesForCircle(38)), ColorOverview(alpha=EMPTY_COLOR, isGlobal=True)), 
                    PolygonClass(regularShape(30, 3), ColorOverview(**RGBtoStaticColor(r=211, g=239, b=246), isGlobal=True)), 
                    PolygonClass(regularShape(10, 3), ColorOverview(alpha=EMPTY_COLOR, isGlobal=True)),), rotationIncrease=1),
                1000000000)
    
    def stopSongs(self, time):
        if self.isMusic and self.MUSIC:
            self.MUSIC.fadeout(time)


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


LEVELS = ((LEVEL0, None), (LEVEL1, 'CorruptedPart1.wav'),
          (LEVEL2, 'CorruptedPart2.wav'), (LEVEL3, 'CorruptedPart3.wav'),
          (LEVEL4, 'CorruptedPart4.wav'), (LEVEL5, 'CorruptedPart5.wav'),
          (LEVEL6, 'CorruptedPart6.wav'), (LEVEL7, 'CorruptedPart7.wav'))

#LEVELS = ((LEVEL7, 'CorruptedPart7.wav'),)
HDMode = True  # <show> whether the game runs on high definition meaning higher quality
GLOBALSOUND = True

def Game(levelUnit=LEVELS):  # <show> Call Function of the game
    pygame.mouse.set_visible(False)
    GameStart = perf_counter()
    Overview.clean()
    global LEVEL
    Overview.BGCOLOR = ColorOverview(
        **RGBtoStaticColor(r=8, g=12, b=14), isGlobal=True, starting=True)
    SCREEN.set_alpha(None)
    program_running = True
    index = 0
    Clock = pygame.time.Clock()
    function = MainMenu
    while index < len(levelUnit):
        level, Music = levelUnit[index]
        #SETUP BLOCK
        Overview.quickClean()
        LEVEL = None
        # <show> Object of Player 1
        P1 = PlayerObject((K_w, K_s, K_a, K_d, K_SPACE))
        program_running = True  # <show> Boolean that tells if the menu is running or not
        Overview.GLOBALFADE.fadeFrom(WHITE, 1)
        Overview.PLAYERS = [P1]  # <show> Holds the List of Players
        # <show> Object of Player 1
        #END OF SETUP BLOCK
        
        #P2 = PlayerObject((K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE))
        level_running = True
        last_dt = perf_counter()
        while level_running:  # <show> While Game is running
            # <show> calculate the movement multiplier for it to be time dependent
            dt = (perf_counter() - last_dt)*FPS
            last_dt = perf_counter()  # <show> last Game Loop time
            Overview.TIMEDELAY = 0
            for event in pygame.event.get():  # <show> for new events happening
                # Start Code Block (can be simplified)
                if event.type == KEYDOWN:  # if a key is pressed down
                    if event.key == K_ESCAPE:  # <show> if new event is quit
                        program_running = False # <show> set the game loop off
                        level_running = False
                        function = MainMenu
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
                    level_running = False
                    function = None
            # GAME LOGIC

            if LEVEL is None:
                if 0 < perf_counter() - GameStart:
                    LEVEL = LevelRunner(level, Music, GLOBALSOUND)
            else:
                if level_running:
                    level_running = not LEVEL.update()

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
                SCREEN.blit(trail.image, Overview.Camera + trail.getScreenPos())

            for bullet in Overview.BULLETS:  # <show> for every Bullet
                # <show> Paste the bullet image at the bullet coordinate on the SCREEN
                SCREEN.blit(bullet.image, Overview.Camera + bullet.getScreenPos())

            for player in Overview.PLAYERS:  # <show> for every Player
                # <show> Paste the player image at the player coordinate on the SCREEN
                SCREEN.blit(player.image, Overview.Camera + player.getScreenPos())
            
            if not len(Overview.PLAYERS):
                level_running = False
                index -= 1

            if HDMode:  # <show> if High Definition Mode is True
                # <show> Display Screen on the Window by scaling it to it's resolution
                DISPLAY.blit(pygame.transform.smoothscale(
                    SCREEN, WINDOW_SIZE), (0, 0))
            else:  # <show> if high Definition Mode is False
                # <show> Display Screen on the Window by smooth scaling it to it's resolution
                DISPLAY.blit(pygame.transform.scale(
                    SCREEN, WINDOW_SIZE), (0, 0))
            pygame.display.update()  # <show> Update the Screen
            Clock.tick()
            pygame.display.set_caption(f'{int(Clock.get_fps())} FPS')
        LEVEL.stopSongs(0)
        if not program_running: break
        index += 1
    return function 


def MainMenu():
    pygame.mouse.set_visible(True)
    framerates = []
    Overview.clean()
    if GLOBALSOUND:
        pygame.mixer.init()
        MUSIC = pygame.mixer.Sound(f'data/Music/MenuMusic.wav')
        MUSIC.set_volume(0.05)
        MUSIC.play(-1)

    last_dt = perf_counter()
    program_running = True  # <show> Boolean that tells if the menu is running or not
    print (convertPointToMid(((0, 94), (754, 94), (754, 0), (44, 0))))
    ButtonObject(
        StaticPoint(1543, 321),
        PolygonOverview(
            (
                PolygonClass(((-377.0, 62.0), (377.0, 62.0), (377.0, -62.0), (-318.0, -62.0)), ColorOverview(
                    **RGBtoStaticColor(r=0, g=0, b=0)), rotationSpeed=1, dimensions=True), 
            ),
            rotation=0,
            rotationIncrease=0
        ), Game, ColorOverview(
            r=DynamicColor(0, 26, 252, DynamicColor.sinColor),
            g=DynamicColor(0, 205, 35, DynamicColor.sinColor),
            b=DynamicColor(0, 232, 114, DynamicColor.sinColor),
        ), Overview.NEXA_BOLD, 86, 'Start', ColorOverview(**RGBtoStaticColor(r=255, g=255, b=255)), (0, 0))
    ButtonObject(
        StaticPoint(1172, 321),
        PolygonOverview(
            (
                PolygonClass(((-39.5, 62.0), (-16.5, 62.0), (39.5, -62.0), (18.5, -62.0)), ColorOverview(
                    r=DynamicColor(0, 26, 252, DynamicColor.sinColor),
                    g=DynamicColor(0, 205, 35, DynamicColor.sinColor),
                    b=DynamicColor(0, 232, 114, DynamicColor.sinColor),
                ), rotationSpeed=1),),
            rotation=0,
            rotationIncrease=0
        ), Game, ColorOverview())

    ButtonObject(
        StaticPoint(1543, 495),
        PolygonOverview(
            (
                PolygonClass(((-377.0, 62.0), (377.0, 62.0), (377.0, -62.0), (-318.0, -62.0)), ColorOverview(
                    **RGBtoStaticColor(r=0, g=0, b=0)), rotationSpeed=1),
            ),
            rotation=0,
            rotationIncrease=0
        ), None, ColorOverview(**RGBtoStaticColor(r=4, g=83, b=87)), Overview.NEXA_BOLD, 64, 'Leave', ColorOverview(**RGBtoStaticColor(r=255, g=255, b=255)), (128, 20))

    ButtonObject(
        StaticPoint(1172, 495),
        PolygonOverview(
            (
                PolygonClass(((-39.5, 62.0), (-16.5, 62.0), (39.5, -62.0), (18.5, -62.0)), ColorOverview(**RGBtoStaticColor(r=4, g=83, b=87)), rotationSpeed=1),),
            rotation=0,
            rotationIncrease=0
        ), None, ColorOverview())

    polygonTimer = perf_counter()  # <show> current time that squares are created
    # <show> Create BackGround Colour
    Overview.BGCOLOR = ColorOverview(**RGBtoStaticColor(r=13, g=21, b=24))
    shake = perf_counter()  # <show> current time when square is created.
    SCREEN.set_alpha(None)
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
                        program_running = False  # <show> return
                        break
            elif event.type == KEYDOWN:  # if a key is pressed down
                if event.key == K_ESCAPE:  # <show> if new event is quit
                    program_running = False  # <show> program sto running
                    function = None
                    break
            elif event.type == QUIT:  # <show> if new event is quit
                program_running = False  # <show> set the game loop off
                function = None
                break
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
            Overview.Camera.blinking(0.2, y=5)  # <show> Screen shake

        for button in Overview.BUTTONS:  # <show> for all buttons
            button.update(dt)  # <show> update button
        for trail in Overview.TRAILS:  # <show> for all trail in Trails
            trail.update(dt)  # <show> update trail
        # Drawing
        # <show> fill Screen with background colour
        SCREEN.fill(Overview.BGCOLOR.giveColorArgs())
        for trail in Overview.TRAILS:
            SCREEN.blit(
                trail.image, Overview.Camera + trail.getScreenPos())

        for button in Overview.BUTTONS:  # <show> for every button
            # <show> Paste the player image at the button coordinate on the SCREEN
            SCREEN.blit(button.image, Overview.Camera + button.getScreenPos())

        if HDMode:  # <show> if High Definition Mode is True
            # <show> Display Screen on the Window by scaling it to it's resolution
            DISPLAY.blit(pygame.transform.smoothscale(
                SCREEN, WINDOW_SIZE), (0, 0))
        else:  # <show> if high Definition Mode is False
            # <show> Display Screen on the Window by smooth scaling it to it's resolution
            DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0))
        pygame.display.update()  # <show> Update the Screen
        framerates.append(1/(perf_counter()-last_dt))
    if GLOBALSOUND:
        MUSIC.fadeout(1000)
    print('')
    print(f'''
Frames: {mean(framerates[10:])}''')
    return function if function else None

if __name__ == '__main__':
    pygame.display.init()
    pygame.font.init()
    WINDOW_SIZE = [i for i in pygame.display.list_modes() if i[0]/16 == i[1]/9][0]
    FPS = 120  # <show> Base Frames Per Second of the Game
    SCREEN_WIDTH = 1920  # <show> pixel Width of the game
    SCREEN_HEIGHT = 1080  # <show> pixel height of the game
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    #WINDOW_SIZE = (1280, 720)  # x, y
    SCREENTODISPLAYSCALAR = tuple(
        win/scr for win, scr in zip(WINDOW_SIZE, SCREEN_SIZE))
    DISPLAYTOSCREENSCALAR = tuple(
        scr/win for win, scr in zip(WINDOW_SIZE, SCREEN_SIZE))

    # <show> Sets the caption of pygame window
    pygame.display.set_caption("Template")
    # Set the Caption Window Like 'Terraria: Also Try Minecraft'
    #DISPLAY = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN | pygame.DOUBLEBUF)  # True Screen
    DISPLAY = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN) #True Screen

    #DISPLAY = pygame.display.set_mode(WINDOW_SIZE)
    # Screen to Blit on other Screen
    SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    currentScreen=MainMenu
    while currentScreen:
        currentScreen = currentScreen()
    pygame.display.quit()




'''

Optimisation
-Multiprocessing


Profiling code

    from pyinstrument import Profiler
    profiler = Profiler()
    profiler.start()
    Game(LEVEL1, 'CorruptedPart1.wav')
    profiler.stop()
    profiler.print()

'''

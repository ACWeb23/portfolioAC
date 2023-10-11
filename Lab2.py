# Global Variables
# declare the screen properties here
TITLE = "Super Mario Kart Lab I"
HEIGHT = 640
WIDTH = 640
STARTSCREEN = True
Paused = True

Track = Actor("track.png",(0,32), anchor =(3.9*WIDTH,2.1*HEIGHT))
Track.x = 0
Track.y = 0
Track.dx = 1
Track.dy = 1

Kart = Actor("mario.png",(WIDTH*0.4,HEIGHT*0.9))
Kart.gasOn = False
Kart.breakOn = False
Kart.coins = 0
TurnRight = False
TurnLeft = False





def draw():
    screen.clear()
    if STARTSCREEN == True:
        screen.clear()
        screen.blit("background1.png", (0,0))
        screen.blit("background2.png", (64,128))
        screen.draw.text("Press Enter To Continue", (160,300), fontsize = 40, color = "red", background = "black")
    else:
        screen.clear()
        Track.draw()
        Kart.draw()

def on_key_down(key):
    global STARTSCREEN, Paused, TurnLeft, TurnRight
    if key == keys.RETURN:
        STARTSCREEN = False
        Paused = False
    if key == keys.ESCAPE:
        STARTSCREEN = not STARTSCREEN
        Paused = not Paused
    if key == keys.W or key == keys.UP:
        Kart.gasOn = True
    if key == keys.S or key == keys.DOWN:
        Kart.gasOn = False
        Kart.breakOn = True
    if key == keys.A or key == keys.LEFT:
        TurnLeft = True
        Kart.image = "mariol.png"
    if key == keys.D or key == keys.RIGHT:
        TurnRight = True
        Kart.image = "marior.png"

def on_key_up(key):
    global STARTSCREEN, Paused
    if key == keys.S or key == keys.DOWN:
        Kart.breakOn = False
    if key == keys.A or key == keys.LEFT:
        TurnLeft = not TurnLeft
        Kart.image = "mario.png"
    if key == keys.D or key == keys.RIGHT:
        TurnRight = not TurnRight
        Kart.image = "mario.png"
    #Flag = not Flag "changes boolean varibles to its opposite"


def update():
    "to be modified later"
    if Kart.gasOn is True:
        Track.y +=1
    if TurnLeft is True:
        Track.x +=1
        print("Left")
    if TurnRight is True:
        Track.x -=1
        print("right")


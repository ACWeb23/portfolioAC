# Write your code here :-)
TITLE = "Super Mario Kart Lab I"
HEIGHT = 640
WIDTH = 640
STARTSCREEN = True

Player1 = Actor("mario.png")
Player1.x = WIDTH*0.4
Player1.y = HEIGHT*0.9
Player1.gasOn = False
Player1.breakOn = False
Player1.coin = 0
Player1.angle = 0


BACKGROUD = Actor("track.png")
BACKGROUD.x = 0
BACKGROUD.y = 0


def draw():
    global STARTSCREEN
    screen.clear()
    if STARTSCREEN is True:
        screen.blit("background1.png", (0 , 0))
        screen.blit("background2.png", (64 , 162))
        screen.draw.text("Press Enter To Continue", (160 , 399), fontsize = 40, color = "red", background = "black")
    if STARTSCREEN is False:
        BACKGROUD.draw()
        Player1.draw()
def on_key_down(key):
    global STARTSCREEN
    if key == keys.RETURN:
        STARTSCREEN = False
    if key == keys.W or key == keys.UP:
        Player1.gasOn = True
        Player1.breakOn = False
        Player1.angle = 0
    if key == keys.S or key == keys.DOWN:
        Player1.breakOn is not Player1.breakOn
        Player1.gasOn is not Player1.gasOn
        Player1.angle = 180
    if key == keys.W and key == keys.D:
        Player1.angle = 315
    if key == key.W and key == keys.A:
        Player1.angle = 45

def on_key_up(key):
    if key == keys.S or key == keys.DOWN:
        Player1.breakOn = False

def update():
    if Player1.gasOn is True and Player1.breakOn is False:
        BACKGROUD.y += 1
        print("Gas")
    if Player1.breakOn is True:
        BACKGROUD.y -= 1
        print("Breaks")

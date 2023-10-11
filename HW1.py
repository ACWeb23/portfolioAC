# COSC 1436 Assignment 1
# Andrew Coleman
# ========================================================================
# World Settings
# ========================================================================
TITLE = "Look to the Sky"
BLOCK_SIZE = 64
H_BLOCKS = 18
V_BLOCKS = 12
WIDTH = BLOCK_SIZE * H_BLOCKS
HEIGHT = BLOCK_SIZE * V_BLOCKS
# ========================================================================
# Actor Creation
# ========================================================================
def init():
    global kite
    kite = Actor("kite.png")
    kite.x = 0
    kite.y = HEIGHT * 0.8
    kite.speed = 1

    global balloon
    balloon = Actor("balloon.png")
    balloon.x = 0
    balloon.y = HEIGHT * 0.4
    balloon.speed = 2

    global dove
    dove = Actor("dove.png")
    dove.x = 0
    dove.y = HEIGHT * 0.6
    dove.speed = 3
# ========================================================================
# Update Function
# ========================================================================

def update():
    kite.x += kite.speed
    kite.x = kite.x % 768

    balloon.x += balloon.speed
    balloon.x = balloon.x % 768

    dove.x += dove.speed
    dove.x = dove.x % 768
# ========================================================================
# Draw Function
# ========================================================================
def draw():
    screen.clear()
    kite.draw()
    balloon.draw()
    dove.draw()
    screen.draw.text("Look To The Sky", topleft=(384,4), fontsize=40)

init()

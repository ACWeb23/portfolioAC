from random import randint
# Global Variables
TITLE = 'Review'
BLOCK_SIZE = 64
WORLD_SIZE = 10
OFFSET = 0.5*BLOCK_SIZE
# Screen is 10 x 11 blocks
WIDTH = WORLD_SIZE*BLOCK_SIZE
HEIGHT = (WORLD_SIZE+1)*BLOCK_SIZE
displayGrid = True  # False: do not show grid, True: show grid
ghosts = []
square = Actor("gridbox.png", anchor = ("left", "top"))
pacman = Actor("pacman.png", (0.5*BLOCK_SIZE, 0.5*BLOCK_SIZE))
pacman.invencible = False
ghostIMG = ["ghost0.png", "ghost1.png", "ghost2.png", "ghost3.png"]
changeLOC = False
IframeTime = 7

def drawGrid():
    for j in range(10):
        square.y = j * 64
        for i in range(10):
            square.draw()
            square.x = i * 64
#power pellet
pellet = Actor("power.png", (randint(0,9)*BLOCK_SIZE+32, randint(0,9)*BLOCK_SIZE+32))
def movePellet():
    global pelletX, pelletY
    if pacman.pos == pellet.pos:
        pacman.invencible = True
        pellet.x = randint(0,9)*BLOCK_SIZE+32
        pellet.y = randint(0,9)*BLOCK_SIZE+32

def InvTime():
    global IframeTime
    if pacman.invencible == True:
        IframeTime -= 1/60
    if IframeTime <= 0:
        pacman.invencible = False
        IframeTime = 7
    print(IframeTime)

# Ghost Creation
for l in range(4):
    ghosts.append(Actor(ghostIMG[l], (BLOCK_SIZE*0.5*WORLD_SIZE - 32, BLOCK_SIZE*0.5*WORLD_SIZE - 32)))
def ghostMove():
    x = randint(0, 100)
    if x == 50:
        for w in range(4):
            ChaseChance = randint(0,3)
            if ChaseChance == 1 or ChaseChance == 2 or ChaseChance == 3:
                if ghosts[w].y < pacman.y:
                    ghosts[w].y += BLOCK_SIZE
                elif ghosts[w].y > pacman.y:
                    ghosts[w].y -= BLOCK_SIZE
                elif ghosts[w].x < pacman.x:
                    ghosts[w].x += BLOCK_SIZE
                elif ghosts[w].x > pacman.x:
                    ghosts[w].x -= BLOCK_SIZE
                if ghosts[w].pos == pacman.pos and pacman.invencible is False:
                    print("Game Over")
                    pacman.pos = (608, 608)
            elif ChaseChance == 0:
                print("random")
                GhostMove = randint(0,5)
                if GhostMove == 1:
                    ghosts[w].x += BLOCK_SIZE
                elif GhostMove == 2:
                    ghosts[w].x -= BLOCK_SIZE
                if ghosts[w].x <= 0:
                    ghosts[w].x = WORLD_SIZE * BLOCK_SIZE - 0.5*BLOCK_SIZE
                if ghosts[w].x >= WORLD_SIZE*BLOCK_SIZE:
                    ghosts[w].x = 0.5* BLOCK_SIZE
                elif GhostMove == 3:
                    ghosts[w].y += BLOCK_SIZE
                elif GhostMove == 4:
                    ghosts[w].y += BLOCK_SIZE
                if ghosts[w].y <= 0:
                    ghosts[w].y = WORLD_SIZE * BLOCK_SIZE - 0.5*BLOCK_SIZE
                if ghosts[w].y >= WORLD_SIZE*BLOCK_SIZE:
                    ghosts[w].y = 0.5* BLOCK_SIZE
def ghostLoop():
    global OFFSET
    for m in range(4):
        ghosts[m].draw()


def draw():
    screen.clear()
    screen.draw.text("Position = " + str(pacman.pos), topleft=(2*BLOCK_SIZE, 10*BLOCK_SIZE), color="yellow", fontsize=40)
    drawGrid()
    pacman.draw()
    ghostLoop()
    if pacman.invencible is False:
        pellet.draw()
#    "screen.blit("power.png", (pelletX,pelletY))"
def on_key_up(key):
    "please replace with your own code"
    if key == keys.DOWN:
        pacman.y += 64
        if pacman.y >= BLOCK_SIZE*WORLD_SIZE:
            pacman.y = 0.5 * BLOCK_SIZE
    elif key == keys.UP:
        pacman.y -= 64
        if pacman.y <= 0:
            pacman.y = WORLD_SIZE * BLOCK_SIZE - 0.5*BLOCK_SIZE
    if key == keys.RIGHT:
        pacman.x += 64
        if pacman.x >= BLOCK_SIZE*WORLD_SIZE:
            pacman.x = 0.5 * BLOCK_SIZE
    elif key == keys.LEFT:
        pacman.x -= 64
        if pacman.x <= 0:
            pacman.x = WORLD_SIZE * BLOCK_SIZE - 0.5*BLOCK_SIZE

def update():
    "please replace with your own code"
    "move()"
    ghostMove()
    movePellet()
    InvTime()
    print(pacman.pos)
    print(pellet.pos)

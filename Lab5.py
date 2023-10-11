# World Settings
TITLE = 'COSC 1436 FPS'
BLOCK_SIZE = 87
WORLD_SIZE = 8
WIDTH = WORLD_SIZE*BLOCK_SIZE
HEIGHT = WORLD_SIZE*BLOCK_SIZE
gameStatus = 0
# 0playing 1 for pause and 2 for game over
# Actor Creation
fps = Actor('crosshair.png')
fps.x = 4*BLOCK_SIZE
fps.y = 4*BLOCK_SIZE
fps.score = 0
fps.ammo = 5
fps.name = 'CS'

gun = Actor('lasergun.png')
gun.visible = False
# using .dx and .dy to change posion in the update function
fps.dx = 0
fps.dy = 0
target = Actor('missile2.png')
target.x = 2*BLOCK_SIZE
target.y = 2*BLOCK_SIZE
target.value = 10
sens = 0.5

# Draw Function

def drawloop():
    target.draw()
    if gun.visible is True:
        gun.draw()
    fps.draw()
    screen.draw.text("Score: " + str(fps.score), topleft=(8, 4), fontsize=40)
    screen.draw.text("Ammo: " + str(fps.ammo), topleft=(WIDTH - 2*BLOCK_SIZE, 4), fontsize=40)
    screen.draw.text("Press I To Change Croshair Speed" , topleft = (WIDTH - 2.5*BLOCK_SIZE, 42), fontsize= 20)

def draw():
    global gameStatus
    screen.clear()
    if gameStatus == 0:
        drawloop()
    elif gameStatus == 1:
        drawloop()
        screen.draw.text("Game Is Paused", topleft = (WIDTH*0.35, HEIGHT*0.4), fontsize = 40)
        screen.draw.text("Press P to Continue", topleft =(WIDTH*0.32, HEIGHT*0.5), fontsize = 40)

# Input

def on_key_down(key):
    global gameStatus
    global sens
    "Need to be completed."
    if gameStatus == 0:
        if key == keys.W or key == keys.UP:
            fps.dy = -1*sens
        if key == keys.S or key == keys.DOWN:
            fps.dy = 1*sens
        if key == keys.D or key == keys.RIGHT:
            fps.dx = 1*sens
        if key == keys.A or key == keys.LEFT:
            fps.dx = -1*sens
        if key == keys.P:
            gameStatus = 1
        if key == keys.V:
            gun.visible = not gun.visible
        if key == keys.I:
            sens += 1
            sens = (sens % 5)+0.5
    elif gameStatus == 1:
        if key == keys.P:
            gameStatus = 0
def on_key_up(key):
    "Need to be completed."
    if key == keys.W or key == keys.UP:
        fps.dy = 0
    if key == keys.S or key == keys.DOWN:
        fps.dy = 0
    if key == keys.D or key == keys.RIGHT:
        fps.dx = 0
    if key == keys.A or key == keys.LEFT:
        fps.dx = 0

# Update function
def update():
    if gameStatus == 0:
        fps.x += fps.dx
        fps.y += fps.dy

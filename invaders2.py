"""
Name: Andrew Coleman
----
CWID: 50298859
----
"""


TITLE = 'COSC 1436 Space Invaders'
BLOCK_SIZE = 64
WORLD_SIZE = 10
WIDTH = WORLD_SIZE*BLOCK_SIZE
HEIGHT = WORLD_SIZE*BLOCK_SIZE
numAliens = 2
gameStatus = 0

# Grid

displayGrid = 0  # 0: do not show grid, 1: show grid
cell = Actor('gridbox.png', anchor=('left', 'top'))
cell.x = 0 * BLOCK_SIZE
cell.y = 0 * BLOCK_SIZE

spaceship = Actor("player1", anchor=('left', 'top'))
spaceship.x = 4.5*BLOCK_SIZE
spaceship.y = 9*BLOCK_SIZE
spaceship.aliens_killed = 0
spaceship.score = 0
spaceship.lives = 2
spaceship.visible = True
spaceship.dx = 0
spaceship.dy = 0
spaceship.fired = False


ALIEN_SPEED = 1
alien1 = Actor("alien11", anchor=('left', 'top'))
alien1.x = 2*BLOCK_SIZE
alien1.y = 2*BLOCK_SIZE
alien1.visible = True
alien1.dx = ALIEN_SPEED
alien1.dy = ALIEN_SPEED

alien2 = Actor("alien21", anchor=('left', 'top'))
alien2.x = 3*BLOCK_SIZE
alien2.y = 2*BLOCK_SIZE
alien2.visible = True
alien2.dx = ALIEN_SPEED
alien2.dy = ALIEN_SPEED


laser = Actor("playerlaser", anchor=('left', 'top'))
laser.x = 0
laser.y = 0
laser.visible = False
laser.dy = 1

# Loading High Score

highscore = 0
file = open("HighScore.txt", "r")
highscore = file.readline()
file.close()
highscore = int(highscore)

def draw():
    screen.clear()
    if laser.visible is True:
        laser.draw()
    spaceship.draw()
    if alien1.visible is True:
        alien1.draw()
    if alien2.visible is True:
        alien2.draw()
    screen.draw.text("Score: " + str(spaceship.score), topleft=(8, 4), fontsize=32)
    # displays score
    screen.draw.text("Lives: " + str(spaceship.lives), topright=(WIDTH-8, 4), fontsize=32)
    # displays lives
    screen.draw.text("Hi-Score: " + str(highscore), midtop=(WIDTH/2, 4), fontsize=32)

def on_key_down(key):
    global gameStatus
    "Need to be completed."
    if gameStatus == 0:
        if key == keys.D or key == keys.RIGHT:
            spaceship.dx = 1*2
        if key == keys.A or key == keys.LEFT:
            spaceship.dx = -1*2
        if key == keys.P:
            gameStatus = 1
        if key == keys.SPACE:
            spaceship.fired = not spaceship.fired
            laser.visible = True

    elif gameStatus == 1:
        if key == keys.P:
            gameStatus = 0
def on_key_up(key):
    if key == keys.D or key == keys.RIGHT:
        spaceship.dx = 0
    if key == keys.A or key == keys.LEFT:
        spaceship.dx = 0

def laserHit():
    import random
    choice = random.randint(1, 2)
    laser.dy = 0
    if choice == 1:
        laser.image = "explosion2.png"
    elif choice == 2:
        laser.image = "explosion1.png"
    clock.schedule(resetLaser, 0.2)

# Update function
def update():
    global highscore
    cycle = 0
    #  Alien Movement
    alien1.x += alien1.dx
    alien2.x += alien2.dx
    if alien1.x == 8*BLOCK_SIZE:
        alien1.dx = alien1.dx * -1
        cycle += 1
    if alien2.x == 9*BLOCK_SIZE:
        alien2.dx = alien2.dx * -1
        cycle += 1
    if alien1.x == 0:
        alien1.dx = alien1.dx * -1
    if alien2.x == BLOCK_SIZE:
        alien2.dx = alien2.dx * -1
    #  Spaceship Movement
    if gameStatus == 0:
        spaceship.x += spaceship.dx
        spaceship.x = spaceship.x % 640
    if spaceship.fired is True:
        laser.visible = True
        laser.x = spaceship.x + 26
        laser.y = spaceship.y
        spaceship.fired = False

    if laser.visible is True:
        laser.y -= laser.dy*5
    if laser.colliderect(alien1) and alien1.visible is True and laser.visible is True:
        print("Hit")
        alien1.visible = False
        spaceship.score += 10
        laserHit()
    elif laser.colliderect(alien2) and alien2.visible is True and laser.visible is True:
        alien2.visible = False
        spaceship.score += 20
        laserHit()
        print("Hit")
    if highscore <= spaceship.score:
        spaceship.score = highscore
        file.open("HighScore.txt", "W")
        file.write(highscore)
        file.close()

    if alien1.visible is False and alien2.visible is False:
        clock.schedule(resetAliens, 1.0)

def resetAliens():
    alien1.visible = True
    alien2.visible = True
    alien1.x = 2*BLOCK_SIZE
    alien1.y = 2*BLOCK_SIZE
    alien2.x = 3*BLOCK_SIZE
    alien2.y = 2*BLOCK_SIZE
    laser.visible = False
def resetLaser():
    laser.image = "playerlaser.png"
    laser.visible = False
    laser.dy = 1

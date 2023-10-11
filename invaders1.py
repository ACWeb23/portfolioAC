"""
PLEASE MAKE SURE TO INSERT YOUR INFORMATION:

Name: Andrew Coleman
----

CWID:
----
"""

TITLE = 'COSC 1436 Space Invaders'
BLOCK_SIZE = 64
WORLD_SIZE = 10
WIDTH = WORLD_SIZE*BLOCK_SIZE
HEIGHT = WORLD_SIZE*BLOCK_SIZE
numAliens = 1
displayGrid = 0  # 0: do not show grid, 1: show grid
cell = Actor('gridbox.png', anchor=('left', 'top'))
cell.x = 0 * BLOCK_SIZE
cell.y = 0 * BLOCK_SIZE

spaceship = Actor('player1.png')
spaceship.x = 5*BLOCK_SIZE
spaceship.y = 9*BLOCK_SIZE
spaceship.aliens_killed = 0
spaceship.score = 0
spaceship.lives = 2


# create alien1 here using the alien11.png here
Alien1 = Actor('alien11.png')
Alien1.x = 1.5*BLOCK_SIZE
Alien1.y = 2.5*BLOCK_SIZE

# create alien2 here using the alien21.png here
Alien2 = Actor('alien21')
Alien2.x = 2.5*BLOCK_SIZE
Alien2.y = 2.5*BLOCK_SIZE

def draw():
    screen.clear()
    if displayGrid == 1:
        drawGrid()
    spaceship.draw()
    Alien1.draw()
    Alien2.draw()
    screen.draw.text("Score: " + str(spaceship.score), topleft=(8, 4), fontsize=40)
    screen.draw.text("Lives: " + str(spaceship.lives), topleft=(512, 4), fontsize=40)


# **************This part of the code does not need to be modified******************#
def drawGrid():
    for column_cell in range(WORLD_SIZE):
        for row_cell in range(WORLD_SIZE):
            cell.x = row_cell * BLOCK_SIZE
            cell.y = column_cell * BLOCK_SIZE
            cell.name = "cell"
            cell.draw()

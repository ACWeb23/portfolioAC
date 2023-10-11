# Write your code here :-)
# Write your code here :-)
'''
Questions
    1. Arrow Keys or W,A,S,D
    2. Soud and 2D Graphics
    3. PlayerX, PlayerY, Ghost"n".x Ghost"n".y, score, lives, gameState,
    difficulty, PlayerState, Ghost"n"State. Collision
'''

Score = 0
Level = 1
Invicible = False
Lives = 2
Collision = False
Pallet = 244
Super_Pallet = 1

PlayerX = 64
PlayerY = 64

GhostX = 512
GhostY = 512

Pallet -= 1
Score += 1

if Pallet == 0 and Super_Pallet == 0:
    Level += 1
    Lives += 1
    if lives >= 3:
        lives = 3
    print("Level Up")

if PlayerX and GhostY == PlayerY:
    Collision = True

if Collision == True:
    lives -= 1
    if lives == 0:
        print("Game Over")
    else:
        f = 64
        PlayerY = 64
        Collision = False
        print("Lives " + str(Lives))
print("End Code")

A = 10
B = 15
print("Before:",A,B)
A = A^B
B = A^B
A = A^B
print("After",A,B)

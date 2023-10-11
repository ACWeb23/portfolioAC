# Write your code here :-)
# mar 21 class
MAXLIVES = 5
numLives= 2

# function Definition
def gainLive(numLives):
    if numLives < MAXLIVES:
        numLives += 1
    return numLives

# calling the Function
numLives = gainLive(numLives)
print(numLives)

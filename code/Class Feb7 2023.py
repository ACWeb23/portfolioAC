# Write your code here :-)

Grades = [ 10, 5, -4, 6, 7, 3, 2, -7, 8, -4, -2, 0, -5, 6,]
for val in Grades:
    if val < 0:
        print(val)

GradesPositive = []
for val in Grades:
    if val >= 0:
        GradesPositive.append(val)
print(GradesPositive)

# new Exercise
StandingNames = ["Bowser", "Mario", "Princess", "Luigi", "Yoshi", "Donkey kong", "Toad", "Koopa Troopa"]
StandingNumber =[1, 2, 3, 4, 5, 6, 7, 8]
StandingScore = [45, 30, 15, 5, 5, 0, 0, 0, 0]
print("\tStandings")
for i in range(len(StandingNumber)):
    print(str(StandingNumber[i]) + "\t" + StandingNames[i] + "\t"+ str(StandingScore[i]))

# Multi dimm Array/List 2D & 3D
# Using the previous exampel with 2D Arrays

ScoreBoard = [["Bowser\t", "Mario\t", "Princess", "Luigi\t", "Yoshi\t", "Donkey kong", "Toad\t", "Koopa Troopa"],[1, 2, 3, 4, 5, 6, 7, 8],[45, 30, 15, 5, 5, 0, 0, 0, 0]]
print("rows = ", len(ScoreBoard))
print("columns = ", len(ScoreBoard[0]))
print("Row 0: ", ScoreBoard[0],"Row 1 ", ScoreBoard[1])
for r in range(len(ScoreBoard)):
    print(r)
    for c in range(len(ScoreBoard[0])):
        print(ScoreBoard[r][c])


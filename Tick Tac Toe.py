# Write your code here :-)
# Tick Tac Toe
Board = [[0,0,0],[0,0,0],[0,0,0]]
Player1 = "X"
Player2 = "O"
Empty = 0
PlayerInput = ["",""]
Row = 0
Column = 0
GameOver = False
Turns = 1

while GameOver is False:
    print("Player1's Turn")
    print("Turn "+ str(Turns))
    while Row<1 or Row>3:
        print("Please Enter a Row From 1 to 3: ")
        Row = int(input())
    Row -= 1
    while Column<1 or Column>3:
        print("Please Enter a Column From 1 to 3: ")
        Column = int(input())
    Column -= 1
    Board[Row][Column] = Player1
    if Board[0][0] == Board[1][0] == Board[2][0] and Board[0][0] != Board[1][0] == Board[2][0]:
        GameOver = True
    elif Board[1][0] == Board[1][1] == Board[1][2]:
        GameOver = True
    elif Board[2][0] == Board[2][1] == Board[2][2]:
        GameOver = True
    elif Board[0][0] == Board[0][1] == Board[0][2]:
        GameOver = True
    elif Board[1][0] == Board[1][1] == Board[1][2]:
        GameOver = True
    elif Board[2][0] == Board[2][1] == Board[2][2]:
        GameOver = True
    elif Board[0][0] == Board[1][1] == Board[2][2]:
        GameOver = True
    elif Board[0][2] == Board[1][1] == Board[2][0]:
        GameOver = True
    if GameOver == True:
        print("game Over")
    Row = 0
    Column = 0
    print("Player2's Turn")
    while Row<1 or Row>3:
        print("Please Enter a Row From 1 to 3: ")
        Row = int(input())
    Row -= 1
    while Column<1 or Column>3:
        print("Please Enter a Column From 1 to 3: ")
        Column = int(input())
    Column -= 1
    Board[Row][Column] = Player2
    if Board[0][0] == Board[1][0] == Board[2][0]:
        GameOver = True
    elif Board[1][0] == Board[1][1] == Board[1][2]:
        GameOver = True
    elif Board[2][0] == Board[2][1] == Board[2][2]:
        GameOver = True
    elif Board[0][0] == Board[0][1] == Board[0][2]:
        GameOver = True
    elif Board[1][0] == Board[1][1] == Board[1][2]:
        GameOver = True
    elif Board[2][0] == Board[2][1] == Board[2][2]:
        GameOver = True
    elif Board[0][0] == Board[1][1] == Board[2][2]:
        GameOver = True
    elif Board[0][2] == Board[1][1] == Board[2][0]:
        GameOver = True
    if GameOver == True:
        print("game Over")
    for r in Board:
        print(r)
    Turns += 1

# Write your code here :-)
print("Please Enter A Value Between 1 and 4 to choose difficuty")
Difficulty = 0
Counter = 0
while Counter == 0:
    Difficulty = int(input("1 For easy, 2 for Medium, 3 for Hard and 4 for Expert "))
    if Difficulty == 1:
        choice = "Easy"
        print("You Selected " + choice)
        Counter = 1
    elif Difficulty == 2:
        choice = "Medium"
        print("You Selected " + choice)
        Counter = 1
    elif Difficulty == 3:
        choice = "Hard"
        print("You Selected " + choice)
        Counter = 1
    elif Difficulty == 4:
        choice = "Expert"
        print("You Selected " + choice)
        Counter = 1

"Lists"

l = [5,7,20,2,10]
print(len(l))
print(l[1])

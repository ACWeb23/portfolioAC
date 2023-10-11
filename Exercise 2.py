# Write your code here :-)
Characters = ["Lumine", "Octavia", "Edward", "George", "Morgana", "Winston", "Focalors"]
CharacterHealth = [10875, 9570, 14450, 12750, 8433, 10750, 15540]
CharacterATK = [212.4,  196.5, 244.1, 221.3, 261.7, 185.6, 234.4]
CharacterCritRate = [0.5, 0.75, 0.25, 0.66, 0.9, 0.7, 0.3]
Wins = 0
Health = 100.0
RoundWon = False
Player1 = ""
PlayerHealth = 0
PlayerATK = 0
PlayerCritRate = 0
PlayerChoice = False
Choice = 0

while PlayerChoice is False:
    Choice = int(input("Press 1-7 to choose a charater "))
    Choice -= 1

    Player1 = Characters[Choice]
    PlayerATK = CharacterATK[Choice]
    PlayerHealth = CharacterHealth[Choice]
    PlayerCritRate = CharacterCritRate[Choice]
    print(Characters[Choice])
    print("Attack = "+ str(CharacterATK[Choice]))
    print("Health = " + str(CharacterHealth[Choice]))
    print("Crit Rate = " + str(CharacterCritRate[Choice]))
    Choose = str(input("Press Y to confirm or any key to choose again " ))
    if Choose == "Y" or Choose == "y":
        PlayerChoice = True
        print(str(Characters[Choice]) + " Selected")
    elif Choose != "Y" or Choose != "y":
        PlayerChoice = False
        print("Please Select another character")
if PlayerHealth > 0:
    print("You Win")
    if PlayerHealth == CharacterHealth[Choice]:
        print("Flawless Victory")



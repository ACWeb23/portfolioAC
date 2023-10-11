# Write your code here :-)
xPos = 168
yPos = 288
counter = 0
initalList = [["r0","r1","r2","r3","r4","r5","r6","r7"],["f0","f1","f2","f3","f4","f5","f6","f7"],["Bowser","Donkey Kong Jr", "Koopa Troopa", "Luigi","Mario","Princess Peach", "Yoshi", "Toad"]]
charaters = []
for i in range(8):
    if i == 3:
        counter = 0
    charater = Actor("r0",(169, 286))
    charater.sideways = initalList[1][i]
    charater.portrait = initalList[0][i]
    charater.name = initalList[2][i]
    charater.x = xPos+(xPos*counter)
    charater.y = yPos
    counter +=1
    charaters.append(actor)


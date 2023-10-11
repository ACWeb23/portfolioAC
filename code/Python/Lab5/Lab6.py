# Global Variables
TITLE = "Super Mario Kart Lab IV"
WIDTH = 768
HEIGHT = 675
ROWS = 2
COLS = 4
MOVHOROZONTAL = 144
MOVERTICAL = 193
# -------- create the Actor selectBox (Section 1) --------- #
selectBox = Actor("p1.png", (169, 204))
selectBox.visible = True
selectBox.flash = True
selectBox.timer = 0
selectBox.cIDr = 0
selectBox.cIDC = 0
selectBox.selected = False

Pause = False
postiion = 0

Images = [[["r0","r1","r2","r3"],["r4","r5","r6","r7"]],[["f0","f1","f2","f3"],["f4","f5","f6","f7"]]]
Names = ["Bowser","Donkey Kong Jr","Koopa Troopa","Luigi","Mario","Princess Peach","Yoshi","Toad"]
# -------- create the 3 needed lists here (Lab 6) --------- #
selectImage = []
col = 0
row = 0
for i in range(8):
    selectImage.append(Images[1][col][row])
    row += 1
    if i==3:
        col = 1
        row = 0

print(selectImage)
print("not list")
notImage = []
col = 0
row = 0
for i in range(8):
    notImage.append(Images[0][col][row])
    row += 1
    if i==3:
        col = 1
        row = 0

print(notImage)

# -------- create a list of 2D Actors for each kart & racer (Lab 6) --------- #
Karts = []
indexX = 0
indexY = 0
imgIndex1 = 0
imgIndex2 = 0
xPos = 168
yPos = 288
for i in range(8):
    x = 0
    actor = Actor(Images[0][imgIndex1][imgIndex2])
    actor.x = xPos
    actor.y = yPos
    actor.fowardImg = selectImage[i]
    actor.rightImg = notImage[i]
    actor.select = False
    Karts.append(actor)
    xPos += 144
    indexX += 1
    imgIndex2 += 1
    if indexX  > 3:
        indexX = 0
        indexY += 1
        xPos = 168
        yPos = 480
        imgIndex1 +=1
        imgIndex2 = 0

# -------- Animate the selection box by completing this function (Section 2) --------- #
def animateSelBox():
    "to be completed in Section 2"
    if selectBox.flash == True:
        selectBox.timer += 1
        if selectBox.timer == 15:
            selectBox.visible = not selectBox.visible
            selectBox.timer = 0

def updateSelection(dc,dr):
    global postiion
    "to be completed in Section 3 & Lab 6"
    x = dc
    y = dr
    "1"
    if x == 0 and y == 0:
        Karts[0].select = True
        printName = Names[0]
        print(printName)
        postiion = 0
    else:
        Karts[0].select = False
    "2"
    if x == 1 and y == 0:
        Karts[1].select = True
        printName = Names[1]
        postiion = 1
    else:
        Karts[1].select = False
    "3"
    if x == 2 and y == 0:
        Karts[2].select = True
        printName = Names[2]
        postiion = 2
    else:
        Karts[2].select = False
    "4"
    if x == 3 and y == 0:
        Karts[3].select = True
        printName = Names[3]
        postiion = 3
    else:
        Karts[3].select = False
    "Row 2"
    "5"
    if x == 0 and y == 1:
        Karts[4].select = True
        printName = Names[4]
        postiion = 4
    else:
        Karts[4].select = False
    "6"
    if x == 1 and y == 1:
        Karts[5].select = True
        printName = Names[5]
        postiion = 5
    else:
        Karts[5].select = False
    "7"
    if x == 2 and y == 1:
        Karts[6].select = True
        printName = Names[6]
        postiion = 6
    else:
        Karts[6].select = False
    "8"
    if x == 3 and y == 1:
        Karts[7].select = True
        printName = Names[7]
        postiion = 7
    else:
        Karts[7].select = False
    "Image Change"
    for i in range(len(Karts)):

        if Karts[i].select is True:
            Karts[i].image = Karts[i].fowardImg
        elif Karts[i].select is False:
            Karts[i].image = Karts[i].rightImg
    # 1)return previous image from portrait to sideways (Lab 6)
    # 2) determine the new index value (Section 3)
    # 3) handle the special cases for cIDr and cIDc (Section 3)
    # 4) update select box position (Section 3)
    # 5) change picture of selected character from sideways to portrait  (Lab 6)

def on_key_down(key):
    "Right"
    global Pause
    if key == keys.RIGHT:
        sounds.beep.play()
        selectBox.x += 144
        selectBox.cIDC += 1
        if selectBox.cIDC >3:
            selectBox.x = 169
            selectBox.cIDC = 0
    elif key == keys.LEFT:
        sounds.beep.play()
        selectBox.x -= 144
        selectBox.cIDC -= 1
        if selectBox.cIDC <0:
            selectBox.x = 601
            selectBox.cIDC = 3
    elif key == keys.UP:
        sounds.beep.play()
        selectBox.y -= 193
        selectBox.cIDr -= 1
        if selectBox.cIDr == -1:
            selectBox.y = 397
            selectBox.cIDr = 1
    elif key == keys.DOWN:
        sounds.beep.play()
        selectBox.y += 193
        selectBox.cIDr += 1
        if selectBox.cIDr == 2:
            selectBox.y = 204
            selectBox.cIDr = 0
    elif key == keys.RETURN:
        sounds.sound1.play()
        selectBox.flash = False
        selectBox.visible = True
    elif key == keys.ESCAPE:
        sounds.sound1.play()
        selectBox.flash = True

v = 108
w = 236
def imageUpdate():
    if Karts[i].select is True:
            Karts[i].image = selectImage[i]
    for z in range(len(Karts)):
        if Karts[z].select is not True:
            Karts[z].image = notImage[z]
def update():
    "to be completed in Section 2 & Section 3"
    animateSelBox()
    updateSelection(selectBox.cIDC,selectBox.cIDr)
    imageUpdate()
def draw():
    screen.clear()
    # Draw the background on the screen (Section 1)
    screen.blit("bg.png",(0,0))
    if selectBox.visible ==True:
        selectBox.draw()
    screen.draw.text("Choose your driver", center=(WIDTH/2, HEIGHT/7), fontname="joystix", fontsize=18, color = "red")
    v = 108
    w = 236
    for i in range(len(Karts)):
        Karts[i].draw()
    screen.draw.text(Names[postiion], (WIDTH * 0.15, HEIGHT * 0.84), fontname="joystix", fontsize=18, color = "green", background = "dimgray")

    screen.draw.text("Press ENTER to select. Press ESCAPE to cancel.", center=(WIDTH//2, HEIGHT*0.94), fontname="joystix", fontsize=16, color = "yellow")


updateSelection(selectBox.cIDr,selectBox.cIDC)

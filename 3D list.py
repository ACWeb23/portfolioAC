# Write your code here :-)
list =[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print("tables: ",len(list))
print("rows: ", len(list[0]))
print("Columns: ", len(list[0][0]))

for table in list: #Outer Loop
    for row in table: #Middle Loop
        for col in row: #Inner Loop
            print(col)
xPos = 0.0
yPos = 0.0

def move(float dx, float dy):
    global xPos, yPos
    xPos += dx
    yPos += dy

# Object Orented Programing
    # Properties
    # Behavior
# Class



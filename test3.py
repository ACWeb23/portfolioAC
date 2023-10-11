# Write your code here :-)
Cell = [5,2,0,7,10,3,1]
Low = 0
x = 0
for i in range(len(Cell)):
        for z in range(len(Cell)):
                if Cell[i] > Cell[x]:
                    Low = Cell[x]
        x += 1
print(Cell)
print(Low)

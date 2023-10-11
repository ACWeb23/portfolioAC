Cards = [9,7,10,4,1,8,5]
for i in range(len(Cards), 0, -1):
    for j in range(0, (len(Cards)-1), 1):
        if Cards[j] > Cards[j+1]:
            temp = Cards[j]
            Cards[j] = Cards[j+1]
            Cards[j+1] = temp
    print(Cards)
print(Cards)

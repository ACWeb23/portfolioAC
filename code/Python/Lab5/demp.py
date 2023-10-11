# Write your code here :-)
health = 43
food == 25

def incrementHealth(health, food):
    health = health + food
    if health >=100:
        health = 100
    return health

def pickLargest(val1,val2):
    if val1>val2:
        return val1
    elif val2> val1:
        return val2
    elif val1 == val2:
        print("equal")
        return 0


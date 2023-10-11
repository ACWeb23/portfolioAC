# Write your code here :-)
# basic search list
a = 0
b = 10
m = (0+10//2 =5)
food[m] > 200 -> a = 0, b = m-1 = 4

def linearSearch(lst, item):
    found = False
    i = 0
    while i < len(lst) and not found:
        if lst[i] == item:
            found = True
        i += 1
    return found

q# Write your code here :-)
UserIDs = ["aj231", "Jg78543", "LM645", "pr4375"]
key = input("Enter Your Id: ")
"if key in UserIDs:"
'    print("Found")'
"else:"
' print("Not Found")'
found = False
for i in range(len(UserIDs)):
    print("Searching")
    if UserIDs[i] == key:
        print("Found")
        found = True
        break
if found is not True:
    print("Incorrect Key")
CharaterAge = [17, 15, 77, 85, 45, 61, 21, 85, 15, 18, 19, 17, 61, 45, 21]
search = int(input("Please Enter Age: "))
counter = 0

for i in CharaterAge:
    if i == search:
        counter += 1
print("Count = ", counter)


oldest = 0
for i in CharaterAge:
    if i > oldest:
        oldest = i
print("Oldest = ", oldest)

youngest = 1000
for i in CharaterAge:
    if i < youngest:
        youngest = i
print("Youngest = ", youngest)

numCount = 0
for i in CharaterAge:
    if i >= 30 and i <= 47:
        numCount += 1
print("Number = ", numCount)

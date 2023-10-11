# Shallow/Deep Copy
names = ["mario", "Luigi", "Peach"]
charaters = names
charaters[1] = "LUIGI"
print("Shallow Copy")
print(names)
print(charaters)
# Modifying charaters changes varibles in names because it is a shallow copy
# Deep Copy Python Code
import copy
names2 = ["Mario", "Luigi", "Peach"]
characters2 = copy.deepcopy(names2) # deep copy
characters2[1] = "LUIGI"
print("Deep Copy")
print(names2)
print(characters2)
#In the deep copy the name of luigi is not in all caps in names2 because the deep copy
# Creates a new list in a seperate location in memory

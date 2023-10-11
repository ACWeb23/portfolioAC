# Write your code here :-)
class Cat:
    def __init__(self, eyeColor, weight, length):
        self.eyeColor = eyeColor
        self.weight = weight
        self.length = length

shadow = Cat("yellow", 4.5, 2.5)

print("Eye Color: ", shadow.eyeColor)
print("Weight: ", shadow.weight)
print("Length: ", shadow.length)

# in c++ pointers are varibles that stores an adress to the location of another varibles

# pointers are initalized by using *

#normal Varibles
# int x;
# float y;
# Cat c:

# Pointers
# int* p1;
# float* p2;
# cat* p3;

# Pointers are used to save Memory and speed up processing;

## Memory
# 2 types Stack and Heap
# Stack: manages functions and their varibles
# Heap: allows the programer to store their created objects

# the stack works in the main function by monitoring the line number and creating varibles
# the heap stores the created varibles and classes

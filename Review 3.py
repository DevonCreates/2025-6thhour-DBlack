#Name:Devon Black
#Class: 6th Hour
#Assignment: HW-R3


#1. import random and print "Hello World!"
import random
print('Hello World')
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
x = random.randint(1,10)
y = random.randint(1,10)
z = random.randint(1,10)
print(x,y,z)
#3. Create a list containing 5 strings listing 5 colors.
color_list = ['Blue', 'Green', 'Red', 'Yellow', 'Purple']
#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
print(random.choice(color_list))
#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if x == y and x == z and y == z:
    print("All are the same numbers")
if x == y and x < z :
    print("X and Y are both the lowest integers")
if x == z and x < y :
    print("X and Z are both the lowest integers")
if y == z and y < x :
    print("Y and Z are both the lowest integers")

if x < y and x < z:
    print('X is the lowest')
elif y < x and y < z:
    print('Y is the lowest')
elif z < x and z < y:
    print('Z is the lowest')
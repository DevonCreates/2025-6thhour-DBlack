#Name:Devon Black
#Class: 6th Hour
#Assignment: HW19
from sys import excepthook

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import Hello_world, addition, animals_list, loop
#2. Call the functions here and run HW19
Hello_world()
addition(2,4,7)
animals_list("Cat", "Dog", "Rabbit", "polar bear", "panda")
loop(33)
#3. Delete all calls for problem 5 in HW16 and run HW19 again.

#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("hello world")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num = int(input("Enter a valid integer: "))
    print(100/num)
except ZeroDivisionError:
    print("You can't divide by zero")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
j = int(input("Enter a number: "))
try:
    print("you entered the number:", j)
except ValueError:
    print("Your number is not a number")
#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
x = 6
while x > 0:
    x -= 1
    print(x)
    if x > 0:
        raise Exception("your number went below 0")
#Name:Devon Black
#Class: 6th Hour
#Assignment: HW9
import random

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
num_list = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
#3. Print the list.
print(num_list)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if num_list[0] >= num_list[1] and num_list[0] >= num_list[2]:
    print("num_list[0] is the greatest")
    num = num_list[0]
elif num_list[1] >= num_list[0] and num_list[1] >= num_list[2]:
    print("num_list[1] is the greatest")
    num = num_list[1]
elif num_list[2] >= num_list[0] and num_list[2] >= num_list[1]:
    print("num_list[2] is the greatest")
    num = num_list[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
print(num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("num is divisible by 2 and 3")
    else: print("num is divisible by 2 but not 3")

else:
    if num % 2 == 0:
        print("num is divisible by 3 but not 2")
    else: print("num is divisible by neither")
#Name: Devon Black
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))
#4. Add a and b together, then divide the sum by c. Print the result.
n = a + b
m = n/c
print(m)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
m_rounded = round(m)
print(m_rounded)
if m_rounded % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#6. Create a list of five different random integers between 1 and 10.
num_list = [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]
print(num_list)
#7. Print the 4th number in the list.
print(num_list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
num_list.append(random.randint(10,10))
print(num_list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
num_list.sort()
print(num_list)
print(num_list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += i
#11. Create a list containing the names of five other students in the classroom.
classroom_list = ["Cash", "Alaya", "Tristan", "Devon", "Ally"]
#12. Create a for loop that individually prints out the names of each student in the list.
for classroom_list in classroom_list:
    print(classroom_list)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
r = 1
for r in range(1,101):
    print(r)
    if r % 10 == 0:
        break
#14. Free space. Do something creative. :)
d = 1
for d in range(1,101):
    if d % 2 == 0:
        print("something creative")
        if d % 3 == 0:
            print("something not creative")
            if d % 4 == 0:
                print("something that is somewhat creative")
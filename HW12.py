#Name:Devon Black
#Class: 6th Hour
#Assignment: HW12
import time
import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.\

i = 0
while i <= 5:
    print(i)
    time.sleep(0.4)
    i += 1
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).

k = 0
while k <= 30:
     print(k)
     time.sleep(0.4)
     k += 2
     
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.

l = 0
while l <= 30:
    l += 1
    if l%3 == 0:
        continue
    print(l)
    time.sleep(0.3)

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
z = random.randint (1,6)
while z <= 6:
    print(z)
    if z == 1:
        break
    z = random.randint(1, 6)
#5. Create a while loop that asks for a number input until the user inputs the number 0.
ask = int(input("Enter 0 to quit"))
while ask != 0:
    ask = int(input("Enter 0 to quit"))
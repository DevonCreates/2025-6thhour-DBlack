#Name:Devon Black
#Class: 6th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def world():
    print("Hello World!")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip():
    global heads
    global tails
    for j in range(1,100):
        coin = random.choice(["Heads", "Tails"])
        if coin == "Heads":
            heads += 1
        else:
            tails += 1
#4. Call the "Hello world" and "Coin Flip" functions here
world()
coin_flip()
#5. Print the final result of heads and tails here
print("Heads:", heads)
print("Tails:", tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["red", "brown", "Black", "Green", "Purple"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def beans():
    if beanBag == []:
        print('beanBag is empty')
    else:
        t = random.choice(beanBag)
        beanBag.remove(t)
        print('You removed the color: ', t)
        bean_pull()
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function

def bean_pull():
    question = str(input('Do you want to continue? (y/n) '))
    if question == "y":
        beans()
    elif question == "n":
        print("Thank you for playing!")
    else:
        print("invalid input. ")
#9. Call the "Bean Pull" function here
beans()
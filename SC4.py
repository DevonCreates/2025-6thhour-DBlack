#Name:Devon Black
#Class: 6th Hour
#Assigment: SC4


#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.
import random
stats = []
def func():
        global stats
        d6 = random.randint(1,6)
        d7 = random.randint(1,6)
        d8 = random.randint(1,6)
        d9 = random.randint(1,6)
        d_list = [d6, d7, d8, d9]
        d_list.sort(reverse=True)
        print(d_list)
        z = d_list[0] + d_list[1] + d_list[2]
        stats.append(z)
def x():
    for y in range(1,7):
        func()
x()
print('statistics:', stats)
#Once that is done, to ensure that the average of the statblock is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (SC5) and print the average.
average = sum(stats)/len(stats)
print('average:', average)
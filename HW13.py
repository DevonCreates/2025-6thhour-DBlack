#Name:Devon Black
#Class: 6th Hour
#Assignment: HW13

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
import time
num = 1
while num <= 100:
    num += 1
    if num % 3 ==0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
enemy_attack_dice = random.randint(1,20)
while Enemy_Dice > Hero_Dice:
    thing4 = int(input("Enemy, enter [0] to roll your dice to attack: "))
    enemy_attack = enemy_attack_dice + enemyDict["Mindflayer"]["AtkMod"]
    if thing4 == 0:
        print("Enemy rolled a " + str(enemy_attack_dice))
    if enemy_attack > partyDict["Shadowheart"]["AC"]:
        Attack = partyDict["Shadowheart"]["Damage"] - enemyDict["Mindflayer"]["HP"]
        print("Enemy attacks " + str(partyDict["Shadowheart"]["Damage"]))
    if enemy_attack_dice < enemyDict["Mindflayer"]["AC"]:
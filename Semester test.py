#Name: Devon Black
#Class: 6th Hour
#Assignment: Semester Project 1

import random

#import time

#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Larian Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).

partyDict = {
    "LaeZel" : {
        "HO" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 18,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "HP" : 32,
        "Init" : 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,10) + random.randint(1,10),
    },
    "Astarion" : {
        "HP" : 40,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,8) + random.randint(1,6) + 4,
    }
}

enemyDict = {
    "Goblin" : {
        "HP" : 7,
        "Init" : 0,
        "AC" : 12,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 2
    },
    "Orc": {
        "HP" : 15,
        "Init": 1,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,12) + 3
    },
    "Troll": {
        "HP" : 84,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 4
    },
    "Mindflayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    },
    "Dragon": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}

#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).

#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses

#3. If the attack hits, roll damage and subtract it from the target's hit points.

#4. The second in initiative rolls to attack (and rolls damage) afterwards.

#5. Repeat steps 2-5 until one of the characters is dead.

Dice = random.randint(1,20)
HeroDice = random.randint(1,20)
Enemy_Dice = random.randint(1,20)
thing1 = int(input("Hero, enter [0] to roll your dice: "))

Hero = partyDict["Shadowheart"]
Enemy = enemyDict["Mindflayer"]
#Who goes first
if thing1 == 0:
    print("Hero rolled a " + str(HeroDice))

thing2 = int(input("Enemy, enter [0] to roll your dice: "))
if thing2 == 0:
    print("Enemy rolled a " + str(Enemy_Dice))

if HeroDice > Enemy_Dice:
    print("Hero goes first")
elif Enemy_Dice > HeroDice:
    print("Enemy goes first")
else:
    print("Hero goes first")
#Attacking
#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses
Heroattackdice = random.randint(18,20)
Enemyattackdice = random.randint(1,20)
while HeroDice >= Enemy_Dice:
    heronewdice = random.randint(1,20)
    enemynewdice = random.randint(1,20)
    int(input("Enter [0] to roll your dice: "))
    if thing1 == 0:
        print("Hero rolled a " + str(heronewdice))
    if Heroattackdice + (partyDict["Shadowheart"]["AtkMod"]) >= (enemyDict["Mindflayer"]["AC"]):
        herohealth = (partyDict["Shadowheart"]["HP"]) - (enemyDict["Mindflayer"]["Damage"])
        enemyhealth = (enemyDict["Mindflayer"]["HP"]) - (partyDict["Shadowheart"]["Damage"])
        print("Hero attacks " + str(partyDict["Shadowheart"]["Damage"]),
                          "Damage from the enemy, enemy has ", + enemyhealth,
                          ("HP remaining"),("Enemy's turn now"))
        print("press [0] to roll ")
        if enemynewdice >= heronewdice:
            print("Enemy rolled " + str(enemynewdice))
            if enemynewdice + (enemyDict["Mindflayer"]["AtkMod"]) > partyDict["Shadowheart"]["AC"]:
               print("Enemy attacks " + str(partyDict["Shadowheart"]["Damage"]),)
    if Heroattackdice + (partyDict["Shadowheart"]["AtkMod"]) < (enemyDict["Mindflayer"]["AC"]):
        print("Hero misses, enemy's turn now,")
while Enemy_Dice >= HeroDice:
    heronewdice1 = random.randint(1,20)
    enemynewdice1 = random.randint(1,20)
    int(input(" enter [0] to roll your dice: "))
    if thing1 == 0:
        print("Enemy rolled a " + str(enemynewdice1))
    if Enemyattackdice + (enemyDict["Mindflayer"]["AtkMod"]) >= (partyDict["Shadowheart"]["AC"]):
        herohealth = (partyDict["Shadowheart"]["HP"]) - (enemyDict["Mindflayer"]["Damage"])
        enemyhealth = (enemyDict["Mindflayer"]["HP"]) - (partyDict["Shadowheart"]["Damage"])
        print("Enemy attacks " + str(enemyDict["Mindflayer"]["Damage"]),
                          "Damage from the Hero, Hero has ", + herohealth,
                          ("HP remaining"),("Hero's turn now"))
        print("press [0] to roll ")
        if heronewdice >= HeroDice:
            print("Enemy rolled " + str(enemynewdice))
            if heronewdice + (partyDict["Shadowheart"]["AtkMod"]) > enemyDict["Mindflayer"]["AC"]:
               print("Hero attacks " + str(partyDict["Shadowheart"]["Damage"]),)
    if Heroattackdice + (partyDict["Shadowheart"]["AtkMod"]) < (enemyDict["Mindflayer"]["AC"]):
        print("Hero misses, enemy's turn now, press [0], to roll your dice ")
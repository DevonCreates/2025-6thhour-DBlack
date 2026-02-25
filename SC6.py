#Name:Devon Black
#Class: 6th Hour
#Assignment: Scenario 6

import random

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)

class Party:
    def __init__(self, Hp, Init, Ac, AtkMod, Damage):
        self.Hp = Hp
        self.Init = Init
        self.Ac = Ac
        self.AtkMod = AtkMod
        self.Damage = Damage
LaeZel = Party(48,1,17,6,random.randint(1,6) + random.randint(1,6) + 3)
Shadowheart = Party(40,1,18,4, random.randint(1,6) + 3)
Gale = Party(32,1,14,6, random.randint(1,10) + random.randint(1,10))
Astarion = Party(40,3,14,5, random.randint(1,8) + random.randint(1,6) + 4)
Goblin = Party(7,0,12,4, random.randint(1,6) + 2)
Orc = Party(15,1,13,5, random.randint(1,12) + 3)
Troll = Party(84,1,15,7, random.randint(1,6) + random.randint(1,6) + 4)
Mindflayer = Party(71,1, 15, 7, random.randint(1,10) + random.randint(1,10) + 4)
Dragon = Party(127,2,18,7, random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4)

# Init Roll
gale_init_roll = random.randint(1,20) + Gale.Init
orc_init_roll = random.randint(1,20) + Orc.Init
if gale_init_roll >= orc_init_roll:
    print("Gale goes first!")
    hero_first = True
else:
    print("Orc goes first!")
    hero_first = False

# Rest of code
if hero_first == True:
    while Gale.Hp > 0 or Orc.Hp > 0:
        gale_atk_roll = random.randint(1, 20)
        if gale_atk_roll == 20:
            print("Critical Hit!")
            Orc.Hp -= (Gale.Damage * 2)
        elif gale_atk_roll == 1:
            print("Critial Miss!")
        elif gale_atk_roll + Gale.AtkMod >= Orc.Ac:
            print("Gale hits!")
            Orc.Hp -= (Gale.Damage)
        elif gale_atk_roll + Gale.AtkMod < Orc.AtkMod:
            print("Gale misses!")

        if Orc.Hp <= 0:
            print("The Orc is dead!")
            break
        else:
            print(f"Orc has {Orc.Hp} HP")

        orc_atk_roll = random.randint(1, 20)
        if orc_atk_roll == 20:
            print("Critical Hit!")
            Gale.Hp -= (Orc.Damage * 2)
        elif orc_atk_roll == 1:
            print("Critical Miss!")
        elif orc_atk_roll + Orc.AtkMod >= Gale.Ac:
            print("Orc hits!")
            Gale.Hp -= Orc.Damage
        elif orc_atk_roll + Orc.AtkMod < Gale.Ac:
            print("Orc misses!")

        if Gale.Hp <= 0:
            print("The Gale is dead!")
            break
        else:
            print(f"Gale has {Gale.Hp} HP.")

elif hero_first == False:
    while Gale.Hp > 0 or Orc.Hp > 0:
        orc_atk_roll = random.randint(1, 20)
        if orc_atk_roll == 20:
            print("Critical Hit!")
            Gale.Hp -= (Orc.Damage * 2)
        elif orc_atk_roll == 1:
            print("Critial Miss!")
        elif orc_atk_roll + Orc.AtkMod >= Gale.Ac:
            print("Orc hits!")
            Gale.Hp -= Orc.Damage
        elif orc_atk_roll + Orc.AtkMod < Gale.Ac:
            print("Orc misses!")

        if Gale.Hp <= 0:
            print("The Gale is dead!")
            break
        else:
            print(f"Gale has {Gale.Hp} HP.")

        gale_atk_roll = random.randint(1, 20)
        if gale_atk_roll == 20:
            print("Critical Hit!")
            Orc.Hp -= (Gale.Damage * 2)
        elif gale_atk_roll == 1:
            print("Critial Miss!")
        elif gale_atk_roll + Gale.AtkMod >= Orc.Ac:
            print("Gale hits!")
            Orc.Hp -= Gale.Damage
        elif gale_atk_roll + Gale.AtkMod < Orc.Ac:
            print("Gale misses!")

        if Orc.Hp <= 0:
            print("The Orc is dead!")
            break
        else:
            print(f"Orc has {Orc.Hp} HP")


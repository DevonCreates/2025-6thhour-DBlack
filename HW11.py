#Name:Devon Black
#Class: 6th Hour
#Assignment: HW11

#1. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg


#import random library
import random
#Create a temperature variable, give it a value (random from 1 to 30).
Temp_var = random.randint(1, 30)
print(Temp_var)
#Make an if statement to see if temperature variable is above 20
#   - If yes, print it's hot
#   - If no, bring it to next if statement
if Temp_var > 20:
    print("its hot")
elif Temp_var > 10:
    print("its mild")
#Make an if statement to see if temperature variable is above 10
#   - If yes, print it's mild
#   - If no, print it's cold
if Temp_var < 10:
    print("it's cold")
#Print "Thank you!" and end the code
print("Thank you!")
HeroDice > Enemy_Dice:
thing3 = int(input("Hero, enter [0] to roll your dice to attack: "))
heroattack = heroattackdice + partyDict["Shadowheart"]["AtkMod"]
if thing3 == 0:
    print("Hero rolled a " + str(heroattackdice))
if heroattack >= enemyDict["Mindflayer"]["AC"]:
    Attack = partyDict["Shadowheart"]["Damage"] - enemyDict["Mindflayer"]["HP"]
    print("Hero attacks " + str(partyDict["Shadowheart"]["Damage"]),
          "Damage from the enemy, enemy has " + str(enemyDict["Mindflayer"]["HP"]), ("HP remaining"))


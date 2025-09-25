#Name:Devon Black
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
Character_PropertiesDict = {
    "Enemy_Character_1" :
        {"Name": "Zombie_Falcon",
         "Height" : 630,
         "Health" : 450,
         "Damage" : 350,
           },
    "Enemy_Character_2":
        {"Name": "Zombie_Ironman",
         "Height" : 640,
         "Health" : 650,
         "Damage" : 750,
        },
    "Enemy_Character_3" :
        {"Name" : "Zombie_Thor",
         "Height" : 660,
         "Health" : 1350,
         "Damage" : 1700,
         },
    "Enemy_Character_4" :
        {"Name" : "Zombie_Hulk",
         "Height" : 1500,
         "Health" : 2250,
         "Damage" : 1200,
         },
    "Enemy_Character_5" :
        {"Name" : "Zombie_Scarlett_Witch",
         "Height" : 580,
         "Health" : 3300,
         "Damage" : 4500,
     },
}
Character_PropertiesDict["Enemy_Character_1"]["Damage"] = int(input("Change enemy 1 damage"))
print(Character_PropertiesDict["Enemy_Character_1"])
Character_PropertiesDict["Enemy_Character_2"]["Damage"] = int(input("Change enemy 2 damage"))
print(Character_PropertiesDict["Enemy_Character_2"])
Character_PropertiesDict["Enemy_Character_3"]["Damage"] = int(input("Change enemy 3 damage"))
print(Character_PropertiesDict["Enemy_Character_3"])
Character_PropertiesDict["Enemy_Character_4"]["Damage"] = int(input("Change enemy 4 damage"))
print(Character_PropertiesDict["Enemy_Character_4"])
Character_PropertiesDict["Enemy_Character_5"]["Damage"] = int(input("Change enemy 5 damage"))
print(Character_PropertiesDict["Enemy_Character_5"])
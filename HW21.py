#Name:Devon Black
#Class: 5th Hour
#Assignment: HW21

#1. Import the random and time libraries
import random, time
#2. Create a class containing a def function that inits self and the 3 attributes health, damage, and speed.
class Apple:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def warrior_loop(self):
        for x in range(10):
            Warrior.health = Warrior.health - random.randint(1, 6)
            print('The new Warrior health is:', Warrior.health)
            time.sleep(1)
    def heals_warrior(self):
        for Warrior.health in range(71):
            Warrior.health = Warrior.health + 30
#3. Make a "warrior" character object with 100 health, 20 damage, and 30 speed. Print the character's initial health below.
Warrior = Apple(100, 20, 30)
print('The Warriors health is:', Warrior.health)
#4. Make a def function within the class that loops 10 times. Within this function,
#make the following loop 10 times: the character takes a random amount of damage from 1 to 6,
#the new health is printed, a time.sleep delay of one second is done. Call the function to the warrior.
Warrior.warrior_loop()
#5. Make a "healer" character object with 60 health, 10 damage, and 30 speed.
healer = Apple(60,10,30)
healer.heals_warrior()
#6. Make a def function within the class that heals the warrior for 30 health. Create an if statement
#that sets the warrior's health to its max (100) if the healing would bring the warrior's health above that.
#Call the function to the healer.


#7. Print the warrior's final health at the very bottom.
print('The Warriors final health is:', Warrior.health)
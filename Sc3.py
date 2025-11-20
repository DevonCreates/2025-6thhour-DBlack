#Name:Devon Black
#Class: 6th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
m = 0
number_of_players = int(input("How many number of players: "))
for i in range(number_of_players):
    print("player",i + 1)
    g = int(input("Enter your rating:"))
    while g > 5 or g < 1:
        print("Pick a valid number between 1 and 5")
        g = int(input("Enter your rating:"))
    else:
        m += g

print(m / number_of_players)
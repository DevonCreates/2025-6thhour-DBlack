#Name:Devon Black
#Class: 6th Hour
#Assignment: HW4


#1. Print Hello World!
print("Hello world")
robot_player_list = ["Powers", "Murray", "Mayfield", "Hurts", "Downs"]
print(robot_player_list)
#2. Append a new name onto the Name List.
robot_player_list.append("Lamb")
print(robot_player_list)
#3. Print out the 4th name on the list.
print(robot_player_list[3])
#4. Create a list with 4 different integers in it.
num_list = [2, 6, 34, 18]
print(num_list)
#5. Insert a new integer into the 2nd spot and print the new list.
num_list.insert(1, 5)
print(num_list)
#6. Sort the list from lowest to highest and print the sorted list.
num_list.sort()
print(num_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
print(sum(num_list[:3]))
#8. Create a list with two strings, two variables, and too boolean values.
mix_list = ("Ray", "Hill", 2, 57, True, False)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(mix_list[int(input())])
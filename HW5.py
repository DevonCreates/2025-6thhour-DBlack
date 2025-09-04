#Name: Devon Black
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
num_list = [7, 4, 8, 45, 32, 45, 12, 23, 98]
print(num_list)
#2. Sort the list from highest to lowest.
num_list.sort(reverse=True)
print(num_list)
#3. Create an empty list.
bet_list = []
#4. Remove the median number from the first list and add it to the second list.
num_list.remove(32)
bet_list.append(32)
#5. Remove the first number from the first list and add it to the second list.
num_list.remove(98)
bet_list.append(98)
#6. Print both lists.
print(num_list)
print(bet_list)
#7. Add the two numbers in the second list together and print the result.
print(sum(bet_list))
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
num_list.insert(3, 32)
num_list.insert(0, 98)
bet_list.remove(32)
bet_list.remove(98)
#9. Sort the first list from lowest to highest and print it.
num_list.sort()
print(num_list)
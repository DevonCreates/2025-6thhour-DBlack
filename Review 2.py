#Name:Devon Black
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print('Hello world')
#2. Create an empty list.
em_list = []
#3. Create a list that contains the names of everyone in the classroom.
class_names = ['Shane', 'Greg', 'Ally', 'tristan', ' Connor', 'Ethan', ' Coach Mack', ' Devon ', 'Alaya']
#4. Print the list from #3, sort the list, then print the list again.
print(class_names)
names_sorted = sorted(class_names)
print(names_sorted)
#5. Append 5 different integers into the empty list from #2 and print the list.
em_list.append(2)
em_list.append(3)
em_list.append(4)
em_list.append(5)
em_list.append(6)
#6. Add together the middle three numbers in the list from #2 and print the result.
a = em_list[1] + em_list[2] + em_list[3]
print(a)
#7. Remove the very first number in the list from #2. Print the new first number.
em_list.pop(0)
print(em_list[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
ValuesDict = {
        'Name' : 'Devon',
        'Grade' : 12,
        'Color' : 'Blue'
}
#9. Using the update function, add a fourth key and value determining your favorite candy.
ValuesDict.update({'Candy' : 'Kitkats'})
#10. Print ONLY the values of the dictionary from #8.
print(ValuesDict.values())
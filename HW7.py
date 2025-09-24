#Name: Devon Black
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
DevonCarDict = {
    "Model" : "Charger",
    "Brand" : "Dodge",
    "Year" : [2020, 2022, 2024]
}
#3. Print the keys of the dictionary from #2.
print(DevonCarDict.keys())
#4. Print the values of the dictionary from #2
print(DevonCarDict.values())
#5. Print one of the three numbers from the list by itself
print(DevonCarDict["Year"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
DevonCarDict.update({"Color" : "Black"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(DevonCarDict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
sixth_hour_class = {
    "Student_1" : {"Name" : "Aaden",
    "Age" : 19,
    "Sports" : True,
},
    "Student_2" : {"Name" : "Alaya",
    "Age" : 14,
    "Sports" : True,
},
    "Student_3" : {"Name" : "Carlos",
    "Age" : 12,
    "Sports" : False,
},
}
#9. Print the names of all three classmates on the same ine.
print(sixth_hour_class["Student_1"]["Name"])
print(sixth_hour_class["Student_2"]["Name"])
print(sixth_hour_class["Student_3"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
sixth_hour_class.pop("Student_3")
print(sixth_hour_class)
#Name:Devon Black
#Class: 6th Hour
#Assignment: HW_R8


#1. Import all of HW_R7 into this assignment using the from/import function.
from Review7 import attributes

#2. Create an object of three students in the classroom. Ask for their name, grade, and favorite color as need be.
First = attributes('Ally', 12, 'Purple')
Second = attributes('Alaya', 9, 'Orange')
Third = attributes('Greg', 12, 'Purple')
#3. Print the name of the first student.
print(First.Name)
#4. Use the def function from HW_R7 to bump the grade level of the second student up by 1. Print the new grade.
Second.add()
print(Second.Grade)
#5. Use the def function from HW_R7 to ask the third student to change their favorite color to something else.
#Print the new color.
Third.change()
print("The Third Student's new favorite color is:", Third.Color)
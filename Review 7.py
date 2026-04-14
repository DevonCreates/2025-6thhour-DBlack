#Name:Devon Black
#Class: 6th Hour
#Assignment: HW_R7


#1. Create a class containing a def function that inits self and the three attributes: name, grade, color.
class attributes:
    def __init__(self, Name, Grade, Color):
        self.Name = Name
        self.Grade = Grade
        self.Color = Color
    def add(self):
        if self.Grade == 12:
            print('You graduated, yay!!')
        else:
            self.Grade += 1
            print('Your are in the', self.Grade, 'Grade')
    def change(self):
        t = input('change the your favorite color?: y/n: ')
        if t == 'y':
            self.Color = input('What would you like to change the color to?: ')
            print('Your new favorite color is:', self.Color)
        elif t == 'n':
            print('Have a good day!')
        else:
            print('choose a valid option')
            self.change()

First = attributes('Devon', 11, 'green')
First.add()
First.change()
#2. Make a def function within the class that adds 1 to the grade attribute to any object called to it.
#If they are 12th grade, have the code change their grade to "graduated" instead.

#3. Make a def function within the class that offers the user to input/change their favorite color.

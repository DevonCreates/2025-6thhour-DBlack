#Name: Devon Black
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class market:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double(self):
        self.cost *= 2
    def stock_fourth(self):
        self.stock *= 1/4
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
'apple = market(50, 1, 1)'
milk = market(25, 3, 1)
chicken = market(36, 6, 4)
#3. Print the stock of all three objects and the cost of the second store item.
print('The stock of the three objects are:', milk.stock, chicken.stock)
print('The banana cost is:', milk.cost)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
milk.double()
print(milk.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
chicken.stock_fourth()
print(chicken.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
try:
    print(apple.weight)
except:
    print('APPLE DOES NOT EXIST')
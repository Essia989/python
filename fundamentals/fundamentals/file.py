
# variable declaration
num1 = 42 # Numbers
num2 = 2.3 # Numbers
boolean = True 
string = 'Hello World' # String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List initialization 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionary initialization
fruit = ('blueberry', 'strawberry', 'banana') # Tuple initialization

print(type(fruit))  #type check
print(pizza_toppings[1]) # access value and printing the value 
pizza_toppings.append('Mushrooms') # adding valus to the list
print(person['name']) 
person['name'] = 'George' # updating value 
person['eye_color'] = 'blue'
print(fruit[2])

if num1 > 45: # conditional if
    print("It's greater")
else: # conditional else 
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:  # conditional if else 
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop printing x from 0 to 4
    print(x)
    print(x)
for x in range(2,5): # for loop printing x from 2 to 4
    print(x)
for x in range(2,10,3):# for loop printing x from 2 to 9 with a step of 3
    print(x)
    print(x)
x = 0 # variable initialization
while(x < 5): # while loop printing x until it's equal to 5
    print(x)
    x += 1

pizza_toppings.pop() # calling function pizza_topping_pop without parameters
pizza_toppings.pop(1) # calling function pizza_topping_pop with 1 as a parameter
print(person) # printing the person Dictionary 
person.pop('eye_color') # deleting the element with the index 'eye_color' from the person Dictionary
print(person) # printing the person Dictionary after the change

for topping in pizza_toppings: # for loop to go through the pizza_toppings 
    if topping == 'Pepperoni':
        continue # for loop continue 
    print('After 1st if statement')
    if topping == 'Olives':
        break # for loop break 

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() # function calling 

def print_hello_x_times(x): # function declaration
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # calling function print_hello_x_times

def print_hello_x_or_ten_times(x = 10): # function declaration 
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
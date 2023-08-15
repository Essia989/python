import random


""" 
print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')

print(type(24))
print(type(3.9))
print(type(3j))

int_to_float = float(35)
float_to_int = int(44.6)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

print(random.randint(2,3265)) # provides a random number between 2 and 5 
"""
#print("Hello " + 42)			# output: TypeError
print("Hello " + str(42))		# output: Hello 42

total = 35
user_val = "26"
# total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61
print(total)


first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.



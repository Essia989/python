#------------------------------------------------------------
#1- Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1
x [1][0] = 15
print (x)
#2
students[0]['last_name']= 'Bryan'
print (students)
#3
sports_directory['soccer'][0] = 'Andres'
print (sports_directory)

z[0]['y'] = 30
print(z)

#------------------------------------------------------------
#2- Iterate Through a List of Dictionaries

def iterateDictionary(some_list):
    for index in some_list:
        for key, value in index.items():
            print(f"Key : {key}, Value :{value}")

my_list =[
    {"United States": "Washington D.C.", "Italy": "Rome", "England": "London","brand": "Ford","model": "Mustang","year": 1964},
    {"United States": "Washington D.C.", "Italy": "Rome", "England": "London","brand": "Ford","model": "FORD","year": 1964},
    {"United States": "Washington D.C.", "Italy": "Rome", "England": "London","brand": "Ford","model": "Audi","year": 1964}
] 

iterateDictionary(my_list)

print('----------------------------------------------------------------')

#------------------------------------------------------------
#3- Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        print(dict[key_name])

iterateDictionary2('model',my_list)
print('----------------------------------------------------------------\n')
iterateDictionary2('first_name', students)
print('----------------------------------------------------------------\n')
iterateDictionary2('last_name', students)
print('----------------------------------------------------------------')

#------------------------------------------------------------
#4- Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for index in some_dict:
        print(f"{len(some_dict[index])} {index.upper()}")
        for key in some_dict[index]:
            print(f"{key}")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

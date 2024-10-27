"""
print("This is another version")

# THis is variable
x = 2
y = 3

# This is conditional statement. 
if x > y:   
    print("Yes, This is true")
else:
    print("No, This is wrong")
"""
"""

This is variable 

x= str("2")
y= str("3.4")

z = x + y 
print(z)
"""

#Global variable 
"""
def amount():
    global g            # Global variable is decleared. 
    x =5
    g = x + 5           # Global variable is intaliazed 
    print("function is called")
    print(s)
    print(g)

s= "Aashish"
amount()
print(g)
"""

# multiple value into a variable. 
"""
x = y = z = 3
print(x)
print(y)
print(z)
"""

#add multiple value. 
"""
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
"""

# print different value of different datatype.
"""
x = 5
y = "Aashish"
print(x,y)
"""

#case sensitive. 
"""
x = 6
print(x)
y = 5
print(y)

"""

#List 
"""
fruits = ["bannana","apple",]
print("This is before adding: ", fruits)
fruits[1] = "orange"
print("This is after adding: ", fruits)

fruits.append("Grappes")
print("This is after adding again: ", fruits)

print("---------List Ended----------")

#Tupple

fruits = ("apple","bannana")
print(fruits[1])

#fruits[1] = "grappes"
"""
# Range 
"""    
x = range(2,10,2)    # range here ( start, stop, step)

y = range(2,10)
for i in y:
    print(i)

"""
      
#dicitionary
"""
student = {
    "name" : ["aashish","Om"],
    "age" : ["21","22"] ,
    "course" : ["aws","python"]
}


print(student["name"])
print(student["age"])
print(student["course"])

print("------This is new add up--------")

#student["name"] = "Om"
#student["grade"] = "bachelor"

#print(student["grade"])
for key, value in student.items():
    print(f"{key}: {value}")

print("Written by myself.")
for key, value in student.items():
    print(f"{key}: {value}")
"""

#Question1

"""
Create a dictionary named person with the following key-value pairs:

	•	name: “John”
	•	age: 25
	•	city: “New York”
Then print the value of the name key.
"""

#Answer1 

"""
person = {
    "name" : "John" ,
    "age" : "25" ,
    "city" : "New York"
}
print(person["name"])
"""

#Question2

"""
Given the following dictionary:
student = {"name": "Alice", "age": 20, "grade": "B"}

	•	Change the grade to "A".
	•	Add a new key-value pair: "course": "Python".
Print the updated dictionary.
"""

#Answer2 

"""
student = {
    "name" : "Alice",
    "age" : "20", 
    "grade" : "B"
}
student["grade"]="A"
student["course"]="Python"

for key,value in student.items():
    print(f"{key}:{value}")
"""

#Question3

"""
Write a program to check if the key "age" exists in the following dictionary:
person = {"name": "Bob", "city": "Chicago"}
"""
#Answer3
"""
person = {
    "name": "Bob",
    "city": "Chicago"
}
person["age"]=21
if "age" in person:
    print("Exist")
else:
    print("Doesn't Exist")

del person["age"]
print("\nCheck again\n")

if "age" in person:
    print("Exist")
else:
    print("Doesn't Exist")
"""

#Question 4 
"""
Given the dictionary:

car = {"brand": "Tesla", "model": "Model S", "year": 2022}

Write a program to print all keys and values in the format:

brand: Tesla  
model: Model S  
year: 2022  
"""
#Answer 4

"""
car = {
    "brand": "Tesla",
    "model": "Model S", 
    "year": 2022
    }

for key,value in car.items():
    print(f"{key}: {value}")
"""

#Question 5

"""
Create a dictionary called library with the following key-value pairs:

	•	"books": ["Python Crash Course", "Clean Code", "The Pragmatic Programmer"]
	•	"location": "City Center"

Print the first book from the books list.
"""

#Answer5

"""
library = {
    "books" : ["Python Crash Course", "Clean Code", "The Pragmatic Programmer"],
    "location" : "City Center"
}
print(library["books"][0])
"""

#Queston 6

"""
Given the following dictionary:

employee = {"name": "David", "age": 30, "position": "Manager"}

	•	Remove the "age" key.
	•	Print the dictionary after removing the key.
"""

#Answer 6

"""
employee = {
    "name": "David", 
    "age": 30, "position": 
    "Manager"
    }

del employee["age"]

print(employee)
"""

#Question 7 

"""
Given:

user = {"username": "tech_guru", "followers": 150}

Write a program to safely access the value of the "bio" key. If the key doesn’t exist,
 print "No bio available".

"""

#Answer 7

user = {
    "username" : "tech_guru",
    "followers": 150
}
user["bio"]= "hellow"

bio = user.get("bio")

if bio:
    print(bio)
else:
    print("Doesn't Exist.")

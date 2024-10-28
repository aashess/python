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
#For Loop 
"""
dic = ["hello","om"]
for index, i in enumerate(dic):
    print(f"index {index}: {i}")
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
"""
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
"""

#class and object.
#in update perspective. 
"""
class car:                          #class is created
    def __init__(self,brand,year):          #constructor which automatically intialized
        self.brand = brand
        self.year = year
    
    def display_info(self):             #self means object instance remember. 
        print(f"This is a {self.brand} car from {self.year}")
    
    def update_info(self,newYear):
        self.year = newYear

car1 = car("toyota",2002)
car2 = car("Mercedes",1959)

car1.display_info()
car2.display_info()

car1.update_info(1999)
car1.display_info()
"""

#Adding if-else condition in Class with object. 
"""
class car:                          #class is created
    def __init__(self,brand,year):          #constructor which automatically intialized
        self.brand = brand
        self.year = year
    
    #def display_info(self):             #self means object instance remember. 
     #   print(f"This is a {self.brand} car from {self.year}")
    
    def is_new(self):
        if self.year >= 2000:
            return True
        else:
            return False

car1 = car("toyota",2002)
car2 = car("Mercedes",1959)

print(car1.is_new())
print(car2.is_new())


#car1.display_info()
#car2.display_info()

#car1.update_info(1999)
#car1.display_info()
"""

#loop in class and object. 
"""
class car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    
    def car_disp(self):
        print(f"This is {self.brand} from {self.year}")

Cars = [
    car("Toyota",2002),
    car("Mercedes",1996)
]

for index in Cars:
    print(index.car_disp())
"""
#Inheritance parent class attributes to child class
"""
class Car: 
    def __init__(self,brand, color):
        self.brand = brand
        self.color = color
        #self.battery = battery

    def disp_info(self):
        print(f"Car is of {self.brand} in {self.color} of {self.battery}% battery.")

class electic_car(Car):
    def __init__(self, brand, color, battery):
        super().__init__(brand, color)
        self.battery = battery
    
    def disp_battery(self):
        print(f"and it have {self.battery}% battery.")

p=electic_car("Toyoto","Yellow",100)

p.disp_info()
p.disp_battery()
"""
#
#
#Question 1
#
#

#Create a parent class Animal and a child class Dog.

#	•	Animal class should have:
#	•	An attribute name.
#	•	A method speak() that prints: "I am an animal."
#	•	Dog class should:
#	•	Inherit from Animal.
#	•	Override the speak() method to print: "Woof! I am a dog."
"""
class animal:
    def __init__(self,name):
        self.name=name

# self is important as it remembers instaces and there value.

    def speak(self):
        print(f"I m an {self.name}.")

class dog(animal):
    def speak(self):
        print(f"This is Dog {self.name}")
    
animal = animal("Leo")
dog = dog("Sher")

animal.speak()
dog.speak()
"""
#Quesiton 2
"""
Create a Vehicle class and a Bike class that inherits from it.

	•	Vehicle class should have:
	•	name and max_speed attributes.
	•	A method display_info() to print the name and speed.
	•	Bike class should:
	•	Inherit from Vehicle.
	•	Add an attribute gear_count and a method display_gears().
#output
    Vehicle: Bicycle, Max Speed: 25 km/h
    Gear Count: 5

"""

class vehicle:
    def __init__(self,name,max_speed):
        self.name=name
        self.max_speed = max_speed
    
    def display_info(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed}")

class bike(vehicle):
    def __init__(self,name,max_speed,gear_count):
        super().__init__(name, max_speed)
        self.gear_count = gear_count
    
    def display_gears(self):
        print(f"Gear Count: {self.gear_count}")

#object create 

vehicle = vehicle("MT15", 130)
bike = bike("Yamaha",145,6)


vehicle.display_info()
bike.display_info()
bike.display_gears()


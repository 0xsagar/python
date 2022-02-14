#!/bin/python3

#Variables and Methods

quote = "Everything is fair in Love & War"
print(quote)
print(quote.upper()) #all letters in uppercase
print(quote.lower()) #all letters in lowercase
print(quote.title()) #first letter in uppercase
print(len(quote))

name = "Sagar" #string
age = 21 #integer int(21)
cgpa = "9.5" #float float(9.5)

print (int(age)) #printing the stored integer
print (int(9.5)) #printing an integer as float

print ("My name is " + name + " and I am " + str(age)  + " years old.") 

age += 1
print (age)
birthday = 1
age += birthday
print (age)

print ('\n')
#Functions
print ("Here is an example of Function")

def who_am_i():
	name = "Heath"
	age = 21
	print ("Name: " + name)

#adding parameters
def add_one_hundred(num):
	print (num + 100)

add_one_hundred(100)

def add(x,y):
	print (x+y)

add(3,7)

def multiply(x,y):
	return x*y
print (multiply(7,7))

def square_root(x):
	print (x ** .5)
square_root(64)

def nl():
	print ('\n')

nl()

#Boolean expressions (True or False)
print ("Boolean Expression")

bool1 = True
bool2 = 3*3==9
bool3 = False
bool4 = 3*3 != 9

print (bool1, bool2, bool3, bool4)
print (type(bool1))

nl()
#Relational and Boolean Operators
greater_than = 7>5
less_than = 5 < 7
greater_than_equal_to = 7>=7
less_than_equal_to = 7<=7

test_and = (7>5) and (5<7) #True
test_and2 = (7>5) and (5>7) #False
test_or = (7>5) or (5<7) #True
test_or2 = (7>5) or (5>7) #True

test_not = not True #False

nl()
#Conditional Statements
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"
print (drink(3))
print (drink(1))

def alcohol(age,money):
	if (age >= 21) and (money>=5):
		return "We're getting a drink!"
	elif (age >= 21) and (money <=5):
		return "Come back with more money!"
	elif (age < 21) and (money >=5):
		return "Nice try kid!"
	else:
		return "You're too poor and too young!"

print (alcohol(21,5))
print (alcohol(21,4))
print (alcohol(20,6))
print (alcohol(20,4))

nl()

#Lists - Have brackets []
movies = ["The Hangover", "3 idiots", "ZNMD", "Rudy", "Forrest Gump"]
print (movies[0]) #first item in the list
print (movies[1:4]) #From 2nd item to 5th item
print (movies[1:]) #from 2nd item onwards
print (movies[:2]) #from beginning and stop at 3rd item 
print (movies[-1]) #last item

print (len(movies))
movies.append("Iron Man")
print (movies)

movies.pop()
print (movies)

movies.pop(0)
print (movies)

nl()
#Tupples - Do not change, ()
grades = ("a", "b", "c", "d")
#cannot be changed
print (grades[1])

nl()
#Looping

#For loops = start to finish of an iterate
veg = ["potato", "spinach", "soya", "ladyfinger"]
for x in veg:
	print (x)

#While loops - Execute as long as true

i = 1
while i < 10:
	print (i)
	i+=1

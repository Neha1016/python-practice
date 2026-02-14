
# TRIANGLE PATTERN

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#  VARIABLES AND DATA TYPES
character_name = "Ankit"
character_age = "22"

print("There one was a man named " + character_name + ",")
print("He was " +  character_age  + " yerars old .")
print("He really liked the name" + character_name + ",")
print("But didn't like being "  + character_age + ",")

# changing the value of variable
character_name = "Jayesh"
character_age = "23"

print("There one was a man named " + character_name + ",")
print("He was " + character_age  + " yerars old .")

# ADD CONCATENATION 

character_name = "Ravi" 
print("He really liked the name " + character_name + ",")
print("But didn't like being "  + character_age + ",")

# string is also used as string variable 
academy_name = "sage university "
print(academy_name)

#string concatenation
print("welcome to  " + academy_name)

# string functions
print(academy_name.lower())
print(academy_name.upper())
print(academy_name.isupper())
print(academy_name.upper().isupper())
print(len(academy_name))
print(academy_name[0])
print(academy_name.index("s")) # passing a parameter
print(academy_name.replace("sage" , "Medicap"))


#WORKING WITH NUMBERS
print(10)
print(2.9776)
print(-2.9897)
print(3 +4)
print(7-3)
print(3*5)
print(5 * 7.8)
print(2/4)
print(3*4 + 5)
print(4 * (3 + 5))
print (10 % 3)
print( 22 % 3)

my_num = 4
print(my_num)
print(str(my_num))
print(str(my_num) + " is  my favourite number ")

my_numb = -5
print(abs(my_num))
print(pow(3,2)) # power of a number
print(max(4,6))
print(min(4,8))
print(round(3.7))

from math import *
print(floor(3.8)) # minimum number
print(ceil(3.2)) # maximum number
print(sqrt(64))

#GETTING USER FROM USER

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! you are " + age)
 
#BUILDING A BASIC CALCULATOR
# FIRST WE CONVERT STRING INTO NUMBER FOR USE INT FUNCTION

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2

print(result)
#result1 = int(num1) +int(num2)
#print(result1)

# Mad lib game

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print ("Roses are " + color)
print(plural_noun + " are blue")

print ("I love " + celebrity)

# PRINT MULTIPLE WORDS ON ON LINE 
print("Hello World!", end=" ")
print("I will print on the same line.")
print("I am", 35, "years old.")


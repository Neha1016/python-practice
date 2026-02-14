# PRINT MULTIPLE WORDS ON ON LINE 
print("Hello World!", end=" ")
print("I will print on the same line.")
print("I am", 35, "years old.")
x = 5
y = "John"
print(x)
print(y)
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# CASTING TYPE CASTING
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Get the Type
# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

# Example
x1 = "John"
# is the same as
x2 = 'John'
print(x1)
print(x2)

# Case-Sensitive
# Variable names are case-sensitive.

# Example
# This will create two variables:

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Camel Case
# Each word, except the first, starts with a capital letter:

# myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

# MyVariableName = "John"

# Snake Case

# Each word is separated by an underscore character:

# my_variable_name = "John"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

# Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:

# Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:

# Example

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:

# Example

x = 5
y = 10
print(x + y)

# x = 5 # string and int we can not  add with + sign
# y = "John"
# print(x + y) # This will produce an error

# which even support different data types:

# Example
x = 5
y = "John"
print(x, y)

#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#if you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#data types
#Print the data type of the variable x:

x = 5
print(type(x))

x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 

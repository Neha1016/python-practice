print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum1)
print(sum2)
print(sum3)

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Python has two division operators:

# / - Division (returns a float)
# // - Floor division (returns an integer)

#Division always returns a float:

x = 12
y = 5

print(x / y)

# Floor division always returns an integer.
# It rounds DOWN to the nearest integer:

x = 18
y = 5

print(x // y)

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Comparison operators return True or False based on the comparison:


x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Test if a number is greater than 0 and less than 10:

x = 5

print(x > 0 and x < 10)

#Test if a number is less than 5 or greater than 10:

x = 5

print(x < 5 or x > 10)

#Reverse the result with not:

x = 5

print(not(x > 3 and x < 10))


#The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#Check if "pineapple" is NOT present in a list:

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

print(6 & 3)
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011

# Then the & operator compares the bits and returns 0010, which is 2 in decimal.

#the | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

print(6 | 3)
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011

# Then the | operator compares the bits and returns 0111, which is 7 in decimal.

#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

print(6 ^ 3)
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011

# Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.


print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))

#Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:

print(100 + 5 * 3)












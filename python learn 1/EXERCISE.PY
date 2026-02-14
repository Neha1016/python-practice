# Mini Task: Write a program that prints your name, college, and career goal.

NAME = "NEHA CHOUHAN"
COLLEGE = "SAGE UNIVERSITY INDORE "
CARRER_GOAL = "DATA SCIENTIST"

print("MY NAME IS " + NAME)
print("MY COLLEGE IS " + COLLEGE)
print("I WANT TO BECOME A " + CARRER_GOAL)

#Mini Task: Write a calculator that adds, subtracts, multiplies, and divides two numbers.
num1 = 10
num2 = 5
addition = num1+num2
substraction = num1-num2
multiplies= num1*num2
divides= num1/num2
print(addition , substraction , multiplies , divides)

#Write a program to check if a word is a palindrome.

word = input("Enter a word:")

reversed_word = word[::-1]

word = word.lower()

if word == reversed_word:
    print( " yes it is palindrome")
    
else:
    print(" no it is not palindrome") 
       
  
  
  #Grade calculator based on marks.
  
marks = int(input("Enter your marks (0-100:"))  
if marks >=90:
    grade = "A"
elif marks >=80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"
    
print("Your grade is:" , grade)  


             
     # Print first 10 Fibonacci numbers

a = 3      # first Fibonacci number
b = 5       # second Fibonacci number

for i in range(5):    # loop will run 10 times for 10 numbers
    print(a)           # print the current number
    c = a + b          # calculate the next Fibonacci number
    a = b              # move 'a' to the next value
    b = c              # move 'b' to the next value
    
    #Make a list of 5 movies and perform CRUD operations.
    
movies = list(("Bajrangi Bhaijan" , "3 Idiots", "Taqdeer" , "Mr Majnu" , "Dangal"))
print(movies)  
movies1 =[] #CREATE
movies1.append("Baghbhan")
movies1.append("PK")
movies1.append("Sultan")
movies1.append("Chhichhore")
movies1.append("Radhe")

print(movies1)             #READ
print(movies1[2])          #READ
movies1[1] = "Lagaan"      #UPDATE
print(movies1)
movies1.remove("Sultan")   #DELETE
print(movies1)
del movies1[0]             #DELETE
print(movies1)

       
       
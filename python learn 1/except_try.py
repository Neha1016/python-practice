# try:
#     number = int(input("Enter a number: "))
#     print(number)
    
    
# except:
#     print("invalid input")
    
    
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
     
except ZeroDivisionError:
     print("divided by zero")
     
except ValueError:
     print("Invalid input")           
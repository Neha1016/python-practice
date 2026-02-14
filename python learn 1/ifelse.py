is_male = False
is_tall = True

if is_male :
    print("You are a male")
else:
    print("You are not a male")   
    
    
    # use or 
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are not  male")   
    
    
    #3 use and
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are not  male or boy ") 
    
    
 # 4
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
    
elif is_male and not(is_tall):
    print("you are a short man")
    
elif not(is_male) and is_tall:
    print("You are not a male but are tall")

else:
    print("You are not a male and not tall")    
    
 # IF STATEMENT AND COMPARISON 
        
def max_num(num1, num2, num3):
     if num1 >= num2 and num1 >= num3:
         return num1
     elif num2 >=num1 and num2>=num3:
         return num2
     else:
         return num3
     
     print(max_num(3,4,5))
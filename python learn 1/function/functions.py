# FUNCTIONS
# GIVING PARAMTER TO FUNCTIONS 
def say_hii(name , age): # function defintion
    print("Hello "+ name +", you are " + age)
    # print("Hello "+ name +", you are " + str(age)) we are also using this
    
print("Top")    
say_hii("Neha", "20") # functions calls 
print("Bottom")
say_hii("Nutan", "21")

# return statement 

def cube(num):
    return num*num*num

result = cube(4)
print(result)

# if statement

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are ma")
else:
    print("You neither male or tall")
    
    

    
    
    
    
    
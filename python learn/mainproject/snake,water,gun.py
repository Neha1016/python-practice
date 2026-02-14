'''
snake = 1
water = -1
gun = 0

'''


computer = -1
youchoice = input("Enter your choice ")
youDict = {"snake":1 , "water":-1 , "gun":0}
reverseDict = {1:"snake" , -1:"water" , 0:"gun"}

you = youDict[youchoice]

print(f"you chose {reverseDict[you]}\n computer choose {reverseDict[computer]}")

if(computer == you ):
    print("Tie")
    
else:    
    if(computer == -1 and you == 1):
      print("you win")    
    
    elif(computer == -1 and you == 0):
      print("you lose")    
    
    elif(computer == 1 and you == -1):
     print("you win")  
      
    elif(computer == 1 and you == 0):
     print("you win")  
      
    elif(computer == 0 and you == 1):
     print("you win")    
    
    elif(computer == 0 and you == -1):
     print("you win")    
 
                

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
for x in "banana":
  print(x) 
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)  
  
for x in range(6):
  print(x)
  
for x in range(2, 6):
  print(x)  
  
for x in range(2, 30, 3):
  print(x)
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")  
  
  #The else block will NOT be executed
  # if the loop is stopped by a break statement.
  
  
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
for x in [0, 1, 2]:
  pass
   
    
# FOR LOOP
    
for letter in "Mahakal Parvati":
    print(letter)
    
        # ARRAY USED
        
friends = ["Ankit", "Chouhan", "Rakesh"] 
for friend in friends:
    print(friend)  
    
 # INDEX USED
friends2 = ["NEHA", "NUTAN", "POOJA"] 
for index in range(10):
    print(friends2)  
         

    
friends4 = ["MAHAKAL","MAHADEV","SHiVSHAMBHU" ] 
for index in range(10):
    print(friends4 , end="")  
    
            
friends4 = ["KRISHNA","MADHAV","SHiV" ] 
#len(friends4)
for index in range(len(friends4)):
    print(friends4[index])  
    
   
friends5 = ["RADHA","RUKMINI","SAI BABA" ]
  
for index in range(5):
      if index == 0:
          print("First Iteration")
      else:
          print("Not first")    
                         
  
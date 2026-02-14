# STRINGS 

a = 'neha'
b = "neha"
c = '''neha'''

print(a,b,c)

name  = "neha"

nameshort = name[0:3]   # start from index 0 all the way till 3 
                        #(exclusive of 3)
print(nameshort)
character1 = name[1]
print(character1)


name1 = "nutan"

print(name1[0:3])

print(name1[-4:-1]) # negative indexing
print(name1[1:4])

print(name1[:4]) # start from index 0 and all the way till 4 (exclusive of 4)
                 
print(name1[1:]) # is same as print(name[1:5])
print(name1[1:5])

# SLICE SKIP VALUE 

word = "amazing"

print(word [1 : 6 : 2]) # start from index 1 and all the way till 6 (exclusive of 6) and skip 2 characters

print(word)

word1 = "amazing"

print(word1[:7]) # word [0:7]
print(word1[0:]) # word [0:7]

# STRING FUNCTION 
# LENGTH 

name2 = "Nutan"
name3 = "nutan"

print(len(name2))
print(name2.endswith("n"))
print(name2.endswith("N"))
print(name2.startswith("Nu"))
print(name2.startswith("nu"))

print(name3.upper())
print(name2.lower())
print(name2.capitalize())

count= name2.count("n")
print(count)

v = name2.find("t")
print(v)

n = "Hello neha "
n = n.replace("neha", "nutan")
print(n)

a = "ankit is a good good boy "
a = a.replace("good", "bad", )
print(a)

#ESCAPR SEQUNCE CHARACTER 

D = " Neha is a good girl \n but not a bad girl"
D1 = " Neha is a good girl \n but \n not a bad girl"
D2 = " Neha is a good girl \t but not a bad girl"
D3 = D = " Neha is a good girl  but not a bad \"girl\""

print(D)
print(D1)
print(D2)
print(D3)



# LIST 


fruits = ["apple", "banana", "cherry", 6, 567.78, True]
print(fruits[0])  # Access first item
print(fruits[-1])  # Access last item
print(fruits[1:4])  # Access a range of items (from index 1 to 3)

fruits[0] = "orange"  # Change the value of the first item
print(fruits[0])


#LIST METHOD 

fruits1 = ["apple", "banana", "cherry", 6, 567.78, True]
print(fruits1)

fruits1.append("grape")
print(fruits1)

l1 = [2,5,7,8, 1 ,4 ,9,65,67]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.pop()
print(l1)
print(l1.pop()) # GIVE RETURN VALUE 

l1.insert(2,88)
print(l1)

l1.remove(88)
print(l1)

# TUPLE 

a = (1, 2, 3, 4, 5)

a1 = () # empty tuple
a2= (1,) # tuple with one item
print(type(a), type(a1), type(a2))

a3 = (23 , False, "neha", 45.67)
print(a3[0]) # Access first item
print(type(a3))

#TUPLE METHOD 

a4 = (23 , False, "neha", 45.67)

print(a4.count(23))  # Count occurrences of 23
print(a4.index("neha"))  # Find index of "neha"
print(len(a4))


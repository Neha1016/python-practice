# DICTIONARY 

marks = {"harry": 90, "rohan": 78, "skillf": 56}
print(marks, type(marks))
print(marks["harry"])

# dict method 

D = {"harry": 90, "rohan": 78, "skillf": 56}

print(marks.keys())
print(marks.values())
print(marks.items())
print(marks.get("harry"))
#print(marks["harry2"]) # give error
print(marks.get("harry2", "Not Found"))
marks.update({"harry": 95})
print(marks)

print(marks.pop("rohan"))
print(marks)
print(marks.popitem())
print(marks)
print(marks.copy())
d = {} # empty dict
    
    
# SET    
s = {1, 2, 3, 4, 4, 3 ,5}
print(s) # set does not allow duplicate values
print(type(s))

s1 = set() # empty set
print(type(s1))

# SET METHOD
s = {1, 2, 3, 4, 4, 3 ,5, "Neha"}
s.add("Nutan")
print(s)
print(len(s))

s.remove(3)
print(s)
s.add(6)
print(s)

v1 = {1,45,6,7}
v2 = {2,3,78,4,1,7}

print(v1.union(v2))
print(v1.intersection(v2))

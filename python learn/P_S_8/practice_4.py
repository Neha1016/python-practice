# sum of natureal number using recursion 

#sum = sum (n-1) + n

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(5))
print(sum(10))

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
    
    
pattern(5)

print("\n")

def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

# Function call must be outside the function definition
pattern(4)

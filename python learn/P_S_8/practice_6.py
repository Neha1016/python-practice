def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the inch value: "))
c = inch_to_cms(n)
print(f" the corresponding value in cms is {c}")

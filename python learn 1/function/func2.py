def raise_to_power (base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num    
    return result

print(raise_to_power(5,5))
    
    
def translate(phrase):
    translation = ""
    for letter in phrase:
        #if letter in "AEIOUaeiou":
        if letter.lower() in "aeiou":  
          if letter.isupper():
            translation = translation + "G"
          else :  
    
            translation = translation + "g"
        else:
            translation = translation + letter 
    return translation

print(translate(input("Enter a phrase: ")))


    
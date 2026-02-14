month_conversion = {"Jan" : "january " , 
                    "Feb" : "February",
                    "Mar" : "March",
    
}

print(month_conversion["Jan"])
print(month_conversion.get("Feb"))
print(month_conversion.get("Abd" , "Not a valid key"))

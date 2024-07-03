age=(int(input("enter your age: ")))
category = ""

if age > 0 : 
    if age <= 12 :
        category = "Child"
    elif age >= 13 and age <= 19 :
        category = "Teenager"
    else :
        category = "adult"    
else :
    category = "your age is invalid"
print(category)
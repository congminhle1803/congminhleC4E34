yob = int(input("Year of birth?: "))
age = 2019 - yob

print("Age: ",age)

if age < 10:
    print("Baby")

elif age < 18:
    print("Teenager")    
else: 
    print("Adult")

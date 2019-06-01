print("Welcome to BMI - Body Mass Index")
height = int(input("Please input your height (cm): "))
height = height/100
weight = int(input("Please input your weight (kg): "))

bmi = weight/(height*height)

print("Your BMI: ",bmi)

if bmi < 16:
    print("Severely underweight")
elif bmi <18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


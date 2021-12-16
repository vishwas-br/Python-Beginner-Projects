print("Hello!")
print("Let's calculate your BMI")
# taking height as input
height = float(input("Enter your height in cm: "))
# taking weight as input
weight = float(input("Enter your weight in kg: "))
# formula for calculating Body Mass Index.
# the value of height taken as input in meters is converted to centimeters
bmi = weight / (height/100)**2
# printing the value of BMI and rounding it off
print(f"Your BMI = {round(bmi,2)}")
# BMI values can tell if you are obese, overweight, healthy or underweight
if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight.")
elif bmi <= 34.9:
    print("You are severely overweight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("You are underweight.")

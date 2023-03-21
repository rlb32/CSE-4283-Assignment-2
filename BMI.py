#Python program to illustrate 
# how to calculate BMI

def BMI(height, weight):
    height = float(height) * 0.025
    print(height)
    weight = float(weight) * 0.45
    round(weight, 1)
    print(weight)
    height = height * height
    bmi = weight/height
    bmi = float(bmi)

    round(bmi, 1)

    return bmi
  
def feetToInches(feet, inches):
    feet = int(feet) * 12
    inches = int(inches)
    height = feet + inches
    return height


    
    

  
# calling the BMI function

print("Welcome to the BMI calculator app!")

feet = input("Please enter your height in feet: ")

inches = input("Now enter the remaining inches: ")

height = feetToInches(feet, inches)

weight = input("Please enter your weight in pounds: ")



bmi = BMI(height, weight)
print("The BMI is", bmi, "so ", end='')
  
# Conditions to find out BMI category
if (bmi < 18.5):
    print("Underweight")
  
elif ( bmi >= 18.5 and bmi < 24.9):
    print("Normal weight")
  
elif ( bmi >= 24.9 and bmi < 30):
    print("Overweight")
  
elif ( bmi >=30):
    print("Obese")
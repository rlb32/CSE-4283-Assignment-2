#Python program to illustrate 
# how to calculate BMI

def BMI(height, weight):
    height = float(height) * 0.025
    weight = float(weight) * 0.45
    round(weight, 1)
    height = height * height
    bmi = weight/height
    bmi = round(bmi, 4)
    

    

    print("The BMI is", bmi, "so ", end='')
  

    if (bmi < 18.5):
        out = print("Underweight")
  
    elif ( bmi >= 18.5 and bmi < 24.9):
        out = print("Normal weight")
  
    elif ( bmi >= 24.9 and bmi < 30):
        out = print("Overweight")
  
    elif ( bmi >=30):
        out = print("Obese")

    return out
  
def feetToInches(feet, inches):
    feet = int(feet) * 12
    inches = int(inches)
    height = feet + inches
    return height


    
    

  
# calling the BMI function and converting height to inches

print("Welcome to the BMI calculator app!")

feet = input("Please enter your height in feet: ")

inches = input("Now enter the remaining inches: ")

height = feetToInches(feet, inches)

weight = input("Please enter your weight in pounds: ")



bmi = BMI(height, weight)

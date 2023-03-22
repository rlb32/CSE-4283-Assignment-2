import BMI
import pytest


def test_BMI_Under_Min_Bound():
    #Testing to see what BMI would output if the BMI was below the Underweight line
    output = BMI.BMI(76, 148.41)
    assert output == "Underweight"


def test_BMI_At_Min_Bound():
    #Testing to see what BMI outputs when the BMI is at the Underweight/Normal weight boundary
    output = BMI.BMI(76, 148.42)
    assert output == "Normal Weight"



def test_BMI_Under_Max_Bound():
    #Testing to see what BMI would output if the BMI was below the Obese line
    output = BMI.BMI(76, 240.66)
    assert output == "Overweight"

def test_BMI_At_Max_Bound():
    #Testing to see what BMI would output if the BMI was at the Obese line   
    output = BMI.BMI(76, 240.67)
    assert output == "Obese"

    

def test_BMI_Under_Middle_Bound():
    #Testing to see what BMI would output if the BMI was below the Underweight line
    output = BMI.BMI(76, 199.75)
    assert output == "Normal Weight"


def test_BMI__At_Middle_Bound():
    #Testing to see what BMI outputs when the BMI is at the Underweight/Normal weight boundary
    output = BMI.BMI(76, 199.76)
    assert output == "Overweight"


def test_Feet_To_Inches():
    #Not a boundary test but just a test to make sure the feet to inches function is working properly
    output = BMI.feetToInches(6, 4)
    assert output == 76

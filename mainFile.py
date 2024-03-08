 #Software Testing homework 2
import pytest

print("Welcome to the BMI Calculator!")

global HeightFeet
global HeightInches
global Weight

#Collect user input for basic variables
try:
    HeightFeet = int(input("Enter your overall height in feet: "))
    HeightInches = int(input("Enter your remaining inches of your overall height: "))
    Weight = int(input("Enter your weight in lbs: "))   
except:
    print("You must input an integer value")
    userMetric()

#Weak 1x1
minimumBoundaryFeet = 3
maximumBoundaryFeet = 8
minimumBoundaryinches = 1
maximumBoundaryinches = 12
minimumBoundaryWeight = 50
MaximumBoundaryWeight = 1000

if HeightFeet > (minimumBoundaryFeet - 1.1) and HeightFeet < (maximumBoundaryFeet+1):
    print("Your variable input  for height in feet is within the boundary limits")
else:
    print("Your feet variable is out of range")
if HeightInches > (minimumBoundaryinches - 1.1 ) and HeightInches < (maximumBoundaryinches+1):
    print("Your variable input  for height in inches is within the boundary limits")
else:
    print("Your inches variable is out of range")
if Weight > (minimumBoundaryWeight - 1.1) and Weight < (MaximumBoundaryWeight+1):
    print("Your variable input  for Weight is within the boundary limits")
else:
    print("Your weight variable is out of range")

#convert overall height to inches
def inches():
    OverallHeightInches = (HeightFeet * 12) + HeightInches
    return OverallHeightInches

#Convert overall height in inches to metric scale
def convertHeight():
    global OverallHeightInches
    OverallHeightInches= inches()
    HeightConversion = OverallHeightInches * .025
    #print("Your Height converted is: ",HeightConversion)
    return HeightConversion

#Convert overall weight to metric system
def convertWeight():
    global WeightConversion
    WeightConversion = Weight * .45
    #print("Your Weight converted it: ", WeightConversion)
    return WeightConversion

#Calculate the BMI
def calculateBmi():

    global heightMeter
    global weightMeter

    #compute bmi
    heightMeter = convertHeight()
    weightMeter = convertWeight()

    Bmi= round(weightMeter/(heightMeter * heightMeter),1)
    print("Your BMI is: ", Bmi)

    return Bmi

#Compare to the scaled system
def checkBmi():

    global BmiCompare

    BmiCompare = calculateBmi()

    if BmiCompare < 18.5:
        print("You are underweight")
        return ("You are underweight")
    if BmiCompare >=18.5 and BmiCompare <= 24.9:
        print("Your bmi is normal")
        return ("Your bmi is normal")
    if BmiCompare >=25 and BmiCompare <= 29.9:
        print("You are overweight")
        return ("You are overweight")
    if BmiCompare > 30:
        print("You are obese")
        return ("You are obese")

#call main function
convertHeight()
convertWeight()
calculateBmi()
checkBmi()
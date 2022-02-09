# This program calculates somebody's Body Mass Index
# Author: Anetta Zak 



weight = float ( input ("Enter your weihgt in kg:") )
height = float ( input ( "Enter your height in cm:") )
height = height/100
BMI = weight/height**2
print ( 'Your BMI is:' , BMI)

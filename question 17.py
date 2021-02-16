'''
17 (Health application: compute BMI) Body mass index (BMI) is a measure of health
based on weight. It can be calculated by taking your weight in kilograms and
dividing it by the square of your height in meters. Write a program that prompts
the user to enter a weight in pounds and height in inches and displays the BMI.
Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters.
Here is a sample run:

Enter weight in pounds:
Enter height in inches:
BMI is 26.8573
50
95.5
Sections
'''

Weight = eval(input("Enter weight in pounds:"))
Height = eval(input("Enter height in inches:"))
WeightInKg = Weight * 0.45359237
HeightInM = Height * 0.0254
BMI = (round((WeightInKg / (HeightInM * HeightInM))* 10000)) / 10000
print("BMI is ",BMI)

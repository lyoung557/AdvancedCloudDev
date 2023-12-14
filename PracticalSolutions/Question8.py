#Q8

"""
Write a program that calculates a person’s BMI (body mass Index) based on their height and weight.
The program should then use conditional statements to determine if the person is underweight, normal weight, overweight,
or obese, and provide appropriate advice on diet and exercise.

"""

height = float(input('Please enter your height in Metres'))
weight = float(input('Please enter your weight in KGs'))

x = weight/float(height*height)
if x < 18.5:
    print('Underweight - You should consult your GP for medical Advice')
elif x>=18.5 and x<25:
    print("Normal - According to your BMI you are healthy keep up the good work")
elif x >= 25 and x < 30:
   print('Overweight - You should consult your GP for medical Advice')
elif x >= 30:
   print('Obesity - You should consult your GP for medical Advice')

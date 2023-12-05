height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = int(weight/height**2)
print("Your BMI is: {}".format(bmi))

# We use '//' for floor division, and round() to round numbers up to x number of decimal plaes

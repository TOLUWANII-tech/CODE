height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = int(weight/height**2)
print("Your BMI is: {bmi}, ")

if bmi<18.5:
    print('Your BMI is: {bmi}, You are underweight')
elif bmi<25:
    print('Your BMI is: {bmi}, You have a normal weight!')
elif bmi<30:
    print('Your BMI is: {bmi}, You hre overwight')
elif bmi<35:
    print('You are obese')
else:
    print('You are clinically overweight1')
print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))
price = 0

if height>120:
    print('You can ride the rollercoaster!')
    age = int(input('How old are you? '))
    if age<12:
        price = 5
        print('Child tickets are #5')
    elif age<=18:
        price = 7
        print('Youth tickets are #7')
    elif (age>=45) & (age<=55):
        print('Everything is going to be okay. Have a free ride on is!')
    else:
        price = 12
        print('Adults tickets are #12')
    

    wants_photo = input("Do you want a photo ticket. Type 'y' for yea and 'n' for no ").lower
    if wants_photo=='y':
        price += 3
        print(f'Your total bill is {price}')
    
    print(f'Your total bll is {price}')


else:
    print('Sorry, you have to grow taller before you can ride')
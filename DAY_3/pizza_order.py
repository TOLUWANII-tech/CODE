print('Welcoe to the Pyton Pizzza Deliivery')
size = input('What size pizza do you want? S, M, or L? ').lower()
add_pepperoni = input('Do you want pepperoni? Y or N? ').lower()
extra_cheese = input('Do you want extra cheese? Y or N? ').lower()

bill = 0

if extra_cheese == 'y': 
    bill+=1



if size=='s':
    bill+=15
    if add_pepperoni == 'y':
        bill+=2
    
elif size=='m':
    bill+=20

    if add_pepperoni == 'y':
        bill+=3 



elif size =='l':
    bill=+25
    if add_pepperoni == 'y':
        bill+=3
    
print(f'Your bill is {bill}')



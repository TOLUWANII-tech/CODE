import random
letters = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print('Welcome to the Pyton Password Generator')

no_of_letters = int(input('How many letters would you like in your password? '))
no_of_numbers = int(input("How many numbers would you like in your password? "))
no_of_symbols = int(input('How many symbols would you like in your password? '))


password_list = []
for letter in range(0, no_of_letters):
    password_list += random.choice(letters)


for symbol in range(0, no_of_symbols):
    password_list += random.choice(symbols)


for number in range(0, no_of_numbers):
    password_list += random.choice(numbers)



random.shuffle(password_list)
password = ''
for character in password_list:
    password+=character

print(password)

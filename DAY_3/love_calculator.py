print('Welcome to the love calculator')
name1 = input('What is your name? \n').lower()
name2 = input('What is their name? \n').lower()
name_combine = name1 + name2

true_letters = str(name_combine.count('t') + name_combine.count('r') + name_combine.count('u') + name_combine.count('e'))

love_letters = str(name_combine.count('l') + name_combine.count('o') + name_combine.count('v') + name_combine.count('e'))

total_score = int(true_letters + love_letters)

if total_score < 10 or total_score >90:
    print(f'Your score is {total_score}, you go together like coke and mentos')
elif total_score > 40 & total_score<50:
    print(f'Your score is {total_score}, you are aright together!')
else:
    print(f'Your score is {total_score}')
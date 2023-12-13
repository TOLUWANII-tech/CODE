import random

print('Welcome to the Number Guessing Game')
print("I'm thinking of anumber between 1 and 100")

correct_answer = random.randint(1, 100)

difficulty_level = input("Choose a difficulty. Type  'easy' or 'hard'").lower()

attempts = 0


def ask_guess():
    user_guess = int(input("Guess a number: "))
    return user_guess


def guess_iteration():
    global attempts
    while attempts > 0:
        print(f"You have {attempts} attempts left to guess the right answer")
        guess = ask_guess()
        if guess == correct_answer:
            print(f"You got it! The answer was {correct_answer}")
            break
        elif guess < correct_answer:
            print("Too low")
        elif guess > correct_answer:
            print("Too high")

        if attempts == 1:
            print("You've run out of guesses, you lose!")
        else:
            print('Guess again.')
        attempts -= 1


if difficulty_level == 'easy':
    attempts = 10
    guess_iteration()
elif difficulty_level == 'hard':
    attempts = 5
    guess_iteration()

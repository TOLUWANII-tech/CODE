import random
import hangman_ascii_art as ha
import hamgman_words as hw



lives = 6
word_list = ['ardvark', 'baboon','camel']
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)

print(chosen_word)
display = []
for letter in chosen_word: 
    display.append('_') 
print(display)

end_of_game = False
#for letter in range(chosen_word_length):
#   display+= '_'
while not end_of_game:

    guess = input('Guess a letter in the word. ').lower()

    # index = -1
    # for letter in chosen_word:
    #     index+=1
    #     if guess == letter:
    #         display[index] = guess
    if guess in display:
        print('You have already guessed that letter')
    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position]= guess
        
    if guess not in chosen_word:
        lives -=1
        print(f'You guessed {guess}. That letter is not in the word, you lose a life!')
        if lives == 0:
            end_of_game = True
            print('You are out of lives, you lose!')

    if not '_' in display:
        end_of_game = True
        print('You win')
    print(display)
    print(ha.stages[lives])


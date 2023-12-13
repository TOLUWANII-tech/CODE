import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def new_game():
    go_on = input(
        "Do you want to play another game of BlackJack? Type 'y' for yes and'n' for no\n> ").lower()
    if go_on == 'y':
        game_iteration()


def deal_card():
    card = random.choice(cards)
    return card


def current_status(user_cards, computer_cards):
    print(f'''
    Your cards are: {user_cards}, current score: {sum(user_cards)}
    Computer's first card: {computer_cards[0]}''')


def final_status(user_cards, computer_cards):
    print(f'''
    Your final hand: {user_cards}, final score: {sum(user_cards)}
    Computer's final hand: {computer_cards}, final computer score : {sum(computer_cards)}
    ''')


def computer_play(user_cards, computer_cards):
    while sum(computer_cards) < 17:
        new_card = deal_card()
        computer_cards.append(new_card)

    final_status(user_cards, computer_cards)
    if sum(user_cards) > 21:
        print("You have gone above 21, you lose!!")
    elif sum(computer_cards) == 21 and sum(user_cards) != 21:
        print(f"Computer has Blackjack! You lose!")
        new_game()


def game_instance(user_cards, computer_cards):
    draw_card = input(
        "Do you want to draw another card? Type 'y' for yes and 'n' for no \n>").lower()
    if draw_card == 'y':
        user_play(user_cards, computer_cards)
    else:
        computer_play(user_cards, computer_cards)
        if sum(computer_cards) > 21:
            print('Computer went over, you win!')
        elif sum(user_cards) > sum(computer_cards):
            print('You win!')
        elif sum(user_cards) < sum(computer_cards):
            print('You lose')
        else:
            print('Draw!')
        new_game()


def user_play(user_cards, computer_cards):
    new_card = deal_card()
    user_cards.append(new_card)
    current_status(user_cards, computer_cards)
    if sum(user_cards) > 21:
        # print(f"{user_cards}, {sum(user_cards)}")

        if 11 in user_cards:
            position = user_cards.index(11)
            user_cards[position] = 1
            current_status(user_cards,  computer_cards)
            if sum(user_cards) > 21:
                computer_play(user_cards, computer_cards)
                new_game()

            else:

                game_instance(user_cards, computer_cards)

        else:
            computer_play(user_cards, computer_cards)
            new_game()

    elif sum(user_cards) == 21:
        computer_play(user_cards, computer_cards)
        print("You have BlackJack! You win!")
        new_game()

    else:
        game_instance(user_cards, computer_cards)


user_blackjack = False
computer_blackjack = False


def game_iteration():
    user_cards_list = [deal_card(), deal_card()]
    computer_cards_list = [deal_card(), deal_card()]

    user_score = sum(user_cards_list)
    computer_score = sum(computer_cards_list)

    current_status(user_cards_list, computer_cards_list)

    if user_score == 21 or computer_score == 21:
        if user_score == 21 and computer_score != 21:
            computer_play(user_cards_list, computer_cards_list)
            print(f"You win, you have Blacjack!!")
        else:
            computer_play(user_cards_list, computer_cards_list)
        new_game()
    else:
        # user_play(user_cards_list, computer_cards_list)
        game_instance(user_cards_list, computer_cards_list)


game_iteration()


# while game_on:
#     new_game = input(
#         "Do youu want to play a game of blackJack. Type 'y' for yes, 'n' for no: ")
#     if new_game == 'y':
#         game_over = False
#     elif new_game == 'n':
#         game_on = False
#         break

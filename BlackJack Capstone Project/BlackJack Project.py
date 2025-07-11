import random
from blackjack_art import logo

Jack = 10
Queen = 10
King = 10
Ace = 1 or 11


def deal_card():
    """Returns a random card from the deck of cards"""
    cards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    """Takes a list of card and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if Ace in cards == 11 and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if c_score == u_score:
        return f"It's a draw both user and computer has a score of {u_score}"
    elif c_score == 0:
        return f"You lose. Opponent has a Blackjack."
    elif u_score == 0:
        return f"You win! Blackjack!"
    elif u_score > 21:
        return f"You went over. You lose."
    elif c_score > 21:
        return f"Opponent went over. You win."
    elif c_score > u_score:
        return f"You lose, Opponent has a score of {c_score}!"
    else:
        return f"You win with a score of {u_score}!"


def play_game():
    print(logo)

    user_card = []
    comp_card = []
    user_score = -1
    comp_score = -1
    is_game_over = False

    for i in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        comp_score = calculate_score(comp_card)
        print(f"Your cards: {user_card}. Current score: {user_score}. ")
        print(f"Computer's first card: {comp_card[0]}. ")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_dealing = input("Type 'y' to get another card, or type 'n' to pass ").lower()
            if continue_dealing == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_card.append(deal_card())
        comp_score = calculate_score(comp_card)

    print(f"User's final hand is {user_card}, final score is {user_score}. ")
    print(f"Computer's final hand is {comp_card}, final score is {comp_score}. ")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of BlackJack? ") == 'y':
    print("\n " * 200)
    play_game()

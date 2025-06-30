
import random

start = "y"

while start == "y":

    print("------------------------------------------------")

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card = []
    dealer_card = []
    next_card = "y"

    player_card.append(random.choice(cards))
    dealer_card.append(random.choice(cards))
    player_card.append(random.choice(cards))
    dealer_card.append(random.choice(cards))

    player_total = player_card[0] + player_card[1]
    dealer_total = dealer_card[0] + dealer_card[1]

    while next_card == "y" and player_total < 22:

        dealer_total = dealer_card[0] + dealer_card[1]
        print(f"Your cards: {player_card}, current score: {player_total}")
        print(f"Dealer first card: {dealer_card[0]}")

        next_card = input("Type 'y' to get another card, type 'n' to pass.  ").lower()

        if next_card == "y":
            player_card.append(random.choice(cards))

        player_total = sum(player_card)

        if player_total > 21 and 11 in player_card:
            player_card.remove(11)
            player_card.append(1)
            player_total = sum(player_card)

        print("------------------------------------------------")

    if player_total > 21:
        print("------------------------------------------------")
        print(f"Your final hand: {player_card}, final score: {player_total}")
        print(f"Dealer final hand: {dealer_card[0], dealer_card[1]}, final score: {dealer_total}")
        print("--------------------YOU LOSE--------------------")

    else:
        if dealer_total > player_total:
            print("------------------------------------------------")
            print(f"Your final hand: {player_card}, final score: {player_total}")
            print(f"Dealer final hand: {dealer_card[0], dealer_card[1]}, final score: {dealer_total}")
            print("--------------------YOU LOSE--------------------")

        elif dealer_total == player_total:
            print("------------------------------------------------")
            print(f"Your final hand: {player_card}, final score: {player_total}")
            print(f"Dealer final hand: {dealer_card[0], dealer_card[1]}, final score: {dealer_total}")
            print("----------------------DRAW----------------------")

        elif dealer_total < player_total:
            print("------------------------------------------------")
            print(f"Your final hand: {player_card}, final score: {player_total}")
            print(f"Dealer final hand: {dealer_card[0], dealer_card[1]}, final score: {dealer_total}")
            print("---------------------YOU WİN---------------------")

    start = str(input("Do you want to play new game of Blackjack? type 'y' or 'n':  ").lower())


import random

# Card and Deck Functions
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(rank):
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)

def hand_value(hand):
    value = 0
    aces = 0
    for rank, _ in hand:
        val = card_value(rank)
        value += val
        if rank == 'A':
            aces += 1
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def show_hand(hand, name, hide_first=False):
    print(f"\n{name}'s Hand:")
    if hide_first:
        print("  [Hidden Card]")
        for card in hand[1:]:
            print(f"  {card[0]} of {card[1]}")
    else:
        for card in hand:
            print(f"  {card[0]} of {card[1]}")
        print(f"  --> Total value: {hand_value(hand)}")

# Main Game Loop
def play_blackjack():
    money = 1000
    print("=== Welcome to Blackjack ===")
    print(f"Starting Balance: ${money}")

    while money > 0:
        print(f"\nYour Balance: ${money}")
        # Bet input with validation
        while True:
            try:
                bet = int(input("Enter your bet (or 0 to quit): $"))
                if 0 <= bet <= money:
                    break
                print("Invalid bet.")
            except ValueError:
                print("Please enter a valid number.")

        if bet == 0:
            print("Thanks for playing!")
            break

        # Deal cards
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        show_hand(dealer_hand, "Dealer", hide_first=True)
        show_hand(player_hand, "Player")

        # Blackjack check
        player_total = hand_value(player_hand)
        dealer_total = hand_value(dealer_hand)
        if player_total == 21:
            show_hand(dealer_hand, "Dealer")
            if dealer_total == 21:
                print("Both have Blackjack! Push.")
            else:
                print("Blackjack! You win 1.5x your bet!")
                money += int(1.5 * bet)
            continue
        elif dealer_total == 21:
            show_hand(dealer_hand, "Dealer")
            print("Dealer has Blackjack! You lose.")
            money -= bet
            continue

        # Player's turn
        while player_total < 21:
            move = input("Hit or Stand? ").lower()
            if move == 'hit':
                player_hand.append(deck.pop())
                show_hand(player_hand, "Player")
                player_total = hand_value(player_hand)
            elif move == 'stand':
                break
            else:
                print("Please type 'hit' or 'stand'.")

        if player_total > 21:
            print("Bust! You lose.")
            money -= bet
            continue

        # Dealer's turn
        show_hand(dealer_hand, "Dealer")
        while dealer_total < 17:
            print("Dealer hits...")
            dealer_hand.append(deck.pop())
            show_hand(dealer_hand, "Dealer")
            dealer_total = hand_value(dealer_hand)

        # Final result
        print(f"\nFinal Scores - Player: {player_total} | Dealer: {dealer_total}")
        if dealer_total > 21 or player_total > dealer_total:
            print("You win!")
            money += bet
        elif dealer_total > player_total:
            print("Dealer wins.")
            money -= bet
        else:
            print("Push. It's a tie.")

    print("\nGame over. You ran out of money!" if money == 0 else "You left with $" + str(money))

if __name__ == "__main__":
    play_blackjack()

import random
import time

# ===== Card Functions =====

def create_deck():
    """Create and shuffle a new 52-card deck."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_name(card):
    return f"{card[0]} {card[1]}"

def blackjack_value(card):
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 1  # Aces counted as 1 initially
    else:         aces -= 1
    return total

# ===== Game Logic =====

def show_hand(hand, hide_first=False):
    if hide_first:
        print(" - [Hidden card]")
        for card in hand[1:]:
            print(" -", card_name(card))
    else:
        for card in hand:
            print(" -", card_name(card))

def blackjack_game():
    money = 100
    deck = create_deck()
    discard_pile = []

    print("=== Welcome to Blackjack ===")

    while True:
        print(f"\nYou have ${money}")
        if money <= 0:
            print("You're out of money!")
            break

        play = input("Do you want to play a hand? (y/n): ").lower()
        if play != 'y':
            break

        # Reshuffle if deck is low
        if len(deck) < 15:
            print("\n--- Reshuffling the deck ---")
            deck.extend(discard_pile)
            discard_pile.clear()
            random.shuffle(deck)

        try:
            bet = int(input("Place your bet: $"))
            if bet <= 0 or bet > money:
                print("Invalid bet.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Deal cards
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print("\nYour hand:")
        show_hand(player_hand)
        print("Total:", hand_value(player_hand))

        print("\nDealer shows:")
        show_hand(dealer_hand, hide_first=True)

        # Player's turn
        while hand_value(player_hand) < 21:
            move = input("\nHit or Stand? (h/s): ").lower()
            if move == 'h':
                new_card = deck.pop()
                player_hand.append(new_card)
                print("You drew:", card_name(new_card))
                print("Your total:", hand_value(player_hand))
                if hand_value(player_hand) > 21:
                    print("You busted!")
                    break
            elif move == 's':
                break
            else:
                print("Invalid input.")

        player_total = hand_value(player_hand)

        # Dealer's turn
        if player_total <= 21:
            print("\nDealer's hand:")
            show_hand(dealer_hand)
            print("Dealer total:", hand_value(dealer_hand))

            while hand_value(dealer_hand) < 17:
                time.sleep(1)
                new_card = deck.pop()
                dealer_hand.append(new_card)
                print("Dealer draws:", card_name(new_card))
                print("Dealer total:", hand_value(dealer_hand))

        dealer_total = hand_value(dealer_hand)

        # Determine outcome
        print("\n--- Result ---")
        if player_total > 21:
            print("You lose!")
            money -= bet
        elif dealer_total > 21 or player_total > dealer_total:
            print("You win!")
            money += bet
        elif dealer_total > player_total:
            print("Dealer wins.")
            money -= bet
        else:
            print("Push (tie).")

        # Move cards to discard
        discard_pile.extend(player_hand)
        discard_pile.extend(dealer_hand)

    print(f"\nGame over. You leave with ${money}. Thanks for playing!")

# ===== Run the Game =====

if __name__ == "__main__":
    blackjack_game()
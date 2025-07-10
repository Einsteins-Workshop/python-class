import random

# Constants
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Deck setup
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def shuffle_deck(deck):
    random.shuffle(deck)

# Calculate hand value with Ace adjustment
def calculate_hand(hand):
    total = 0
    aces = 0
    for rank, _ in hand:
        total += values[rank]
        if rank == 'A':
            aces += 1
    # Adjust Aces from 11 to 1 if needed
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Display hands
def show_hand(name, hand, hide_first_card=False):
    if hide_first_card:
        print(f"{name}'s Hand: [Hidden], {hand[1]}")
    else:
        cards = ', '.join([f"{r} of {s}" for r, s in hand])
        print(f"{name}'s Hand: {cards} (Total: {calculate_hand(hand)})")

# Game logic
def play_blackjack():
    deck = create_deck()
    shuffle_deck(deck)

    # Deal initial hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Show hands
    show_hand("Dealer", dealer_hand, hide_first_card=True)
    show_hand("Player", player_hand)

    # Player's turn
    while True:
        choice = input("Hit or Stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            show_hand("Player", player_hand)
            if calculate_hand(player_hand) > 21:
                print("You busted! Dealer wins.")
                return
        elif choice == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    # Dealer's turn
    print("\nDealer's turn:")
    show_hand("Dealer", dealer_hand)
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        show_hand("Dealer", dealer_hand)
        if calculate_hand(dealer_hand) > 21:
            print("Dealer busted! You win!")
            return

    # Final comparison
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    print(f"\nFinal Scores - Player: {player_total}, Dealer: {dealer_total}")

    if player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_blackjack()

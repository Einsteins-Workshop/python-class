import random

# Card values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Create and shuffle deck
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def shuffle_deck(deck):
    random.shuffle(deck)

# Calculate hand value
def calculate_hand(hand):
    total = 0
    aces = 0
    for rank, _ in hand:
        total += values[rank]
        if rank == 'A':
            aces += 1
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Display hands
def show_hand(name, hand, hide_first=False):
    if hide_first:
        print(f"{name}'s Hand: [Hidden], {hand[1][0]} of {hand[1][1]}")
    else:
        cards = ', '.join(f"{rank} of {suit}" for rank, suit in hand)
        total = calculate_hand(hand)
        print(f"{name}'s Hand: {cards} (Total: {total})")

# Betting and game loop
def play_blackjack():
    chips = 100  # Starting chips
    print("🎲 Welcome to Blackjack with Betting!")
    print(f"You start with ${chips} in chips.")

    while chips > 0:
        print(f"\n💵 Current chips: ${chips}")
        try:
            bet = int(input("Place your bet: $"))
            if bet <= 0 or bet > chips:
                print("Invalid bet amount.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        # Setup deck and hands
        deck = create_deck()
        shuffle_deck(deck)
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Show initial hands
        show_hand("Dealer", dealer_hand, hide_first=True)
        show_hand("Player", player_hand)

        # Player's turn
        while True:
            if calculate_hand(player_hand) == 21:
                print("Blackjack!")
                break
            move = input("Hit or Stand? (h/s): ").lower()
            if move == 'h':
                player_hand.append(deck.pop())
                show_hand("Player", player_hand)
                if calculate_hand(player_hand) > 21:
                    print("Bust! You lose.")
                    chips -= bet
                    break
            elif move == 's':
                break
            else:
                print("Invalid input. Enter 'h' or 's'.")

        # Dealer's turn if player hasn't busted
        if calculate_hand(player_hand) <= 21:
            print("\nDealer's turn:")
            show_hand("Dealer", dealer_hand)
            while calculate_hand(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                show_hand("Dealer", dealer_hand)

            player_total = calculate_hand(player_hand)
            dealer_total = calculate_hand(dealer_hand)

            # Compare hands
            if dealer_total > 21 or player_total > dealer_total:
                print("You win!")
                chips += bet
                chips += bet
                chips += bet
            elif player_total < dealer_total:
                print("Dealer wins.")
                chips -= bet
            else:
                print("Push (Tie). Bet returned.")

        if chips <= 0:
            print("\nYou're out of chips. Game over.")
            break

        again = input("\nPlay another round? (y/n): ").lower()
        if again != 'y':
            print(f"You leave the game with ${chips} in chips.")
            break

if __name__ == "__main__":
    play_blackjack()

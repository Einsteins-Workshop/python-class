import random
import time

# ====== Card & Deck Functions ======

def create_deck():
    """Create and shuffle a standard 52-card deck."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_name(card):
    """Return a string representation of a card."""
    return f"{card[0]} of {card[1]}"

def card_value(card):
    """Return the Blackjack value of a card."""
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 1
    else:
        return int(rank)

def hand_value(hand):
    """Calculate the best Blackjack value for a hand."""
    total = 0
    aces = 0

    for card in hand:
        value = card_value(card)
        total += value
        if card[0] == 'A':
            aces += 1

    # Convert Aces from 1 to 11 as long as it doesn't bust
    while aces > 0 and total + 10 <= 21:
        total += 10
        aces -= 1

    return total

def show_hand(hand, hidden=False):
    """Display cards in a hand."""
    if hidden:
        print(" - [Hidden Card]")
        for card in hand[1:]:
            print(" -", card_name(card))
    else:
        for card in hand:
            print(" -", card_name(card))

# ====== Game Logic ======

def play_blackjack():
    money = 200
    deck = create_deck()
    discard_pile = []

    print("=== Welcome to Blackjack ===")

    while money > 0:
        print(f"\nYou have ${money}")
        play = input("Play a hand? (y/n): ").lower()
        if play != 'y':
            break

        # Reshuffle deck if needed
        if len(deck) < 15:
            print("\n-- Reshuffling deck --")
            deck.extend(discard_pile)
            discard_pile.clear()
            random.shuffle(deck)

        # Take bet
        try:
            bet = int(input("Place your bet: $"))
            if bet <= 0 or bet > money:
                print("Invalid bet.")
                continue
        except ValueError:
            print("Enter a number.")
            continue

        # Deal cards
        player = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]

        print("\nYour hand:")
        show_hand(player)
        print("Total:", hand_value(player))

        print("\nDealer shows:")
        show_hand(dealer, hidden=True)

        # Player turn
        while hand_value(player) < 21:
            move = input("\nHit or Stand? (h/s): ").lower()
            if move == 'h':
                new_card = deck.pop()
                player.append(new_card)
                print("You drew:", card_name(new_card))
                print("Total:", hand_value(player))
                if hand_value(player) > 21:
                    print("Bust! You lose.")
                    money -= bet
                    break
            elif move == 's':
                break
            else:
                print("Invalid input.")

        # Dealer turn
        if hand_value(player) <= 21:
            print("\nDealer's turn:")
            show_hand(dealer)
            while hand_value(dealer) < 17:
                time.sleep(1)
                new_card = deck.pop()
                dealer.append(new_card)
                print("Dealer drew:", card_name(new_card))
                print("Dealer total:", hand_value(dealer))

            player_total = hand_value(player)
            dealer_total = hand_value(dealer)

            print("\n--- Result ---")
            print("Your total:", player_total)
            print("Dealer total:", dealer_total)

            if dealer_total > 21 or player_total > dealer_total:
                print("You win!")
                money += bet
            elif dealer_total > player_total:
                print("Dealer wins.")
                money -= bet
            else:
                print("Push (tie). No money lost.")

        # Discard used cards
        discard_pile.extend(player + dealer)

    print(f"\nGame over! You leave with ${money}. Thanks for playing!")

# ====== Run the Game ======
if __name__ == "__main__":
    play_blackjack()
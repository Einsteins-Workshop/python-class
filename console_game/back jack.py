import random
import os
import time

# ----------------- Utilities -----------------

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(msg="Press Enter to continue..."):
    input(msg)

# ----------------- Card & Deck -----------------

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {rank: min(10, idx+2) if rank != 'A' else 11 for idx, rank in enumerate(ranks)}

def deal_card():
    return random.choice(ranks), random.choice(suits)

def calculate_total(hand):
    total = sum(values[card[0]] for card in hand)
    # Adjust for Aces
    aces = sum(1 for card in hand if card[0] == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# ----------------- ASCII Card -----------------

def print_card(card):
    rank, suit = card
    if rank == '10':
        spacing = ''
    else:
        spacing = ' '
    return f"""
┌─────────┐
│{rank}{spacing}       │
│         │
│    {suit}    │
│         │
│       {spacing}{rank}│
└─────────┘
"""

def display_hand(hand, hide_first=False):
    lines = ['' for _ in range(7)]
    for idx, card in enumerate(hand):
        if idx == 0 and hide_first:
            card_lines = [
                "┌─────────┐",
                "│░░░░░░░░░│",
                "│░░░░░░░░░│",
                "│░░HIDDEN░│",
                "│░░░░░░░░░│",
                "│░░░░░░░░░│",
                "└─────────┘",
            ]
        else:
            card_lines = print_card(card).split('\n')[1:-1]
        for i in range(7):
            lines[i] += card_lines[i] + ' '
    for line in lines:
        print(line)

# ----------------- Game Logic -----------------

def blackjack():
    balance = 1000000000000000000000000000000000000000000000000000000

    while True:
        clear()
        print("=== 🃏 Blackjack with Betting ===")
        print(f"💰 Balance: ${balance}")
        try:
            bet = int(input("Enter your bet (or 0 to quit): $"))
        except ValueError:
            print("Invalid input.")
            continue

        if bet == 0:
            print("Thanks for playing!")
            break
        if bet < 0 or bet > balance:
            print("Invalid bet amount.")
            pause()
            continue

        # Deal hands
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]

        # Gameplay loop
        while True:
            clear()
            print(f"💰 Balance: ${balance} | 🪙 Bet: ${bet}")
            print("\n🧑 Your Hand:")
            display_hand(player_hand)
            print(f"Total: {calculate_total(player_hand)}")

            print("\n🧑‍✈️ Dealer's Hand:")
            display_hand(dealer_hand, hide_first=True)

            total = calculate_total(player_hand)
            if total == 21:
                print("🎉 Blackjack!")
                break



            action = input("\n(H)it or (S)tand? ").lower()
            if action == 'h':
                player_hand.append(deal_card())
            elif action == 's':
                break
            else:
                print("Invalid input.")
                pause()

        # Dealer logic
        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)

        if player_total <= 21:
            while dealer_total < 17:
                dealer_hand.append(deal_card())
                dealer_total = calculate_total(dealer_hand)

        # Final Result
        clear()
        print(f"💰 Balance: ${99999999999999999999999999999999999999} | 🪙 Bet: ${bet}")
        print("\n🧑 Your Final Hand:")
        display_hand(player_hand)
        print(f"Total: {player_total}")

        print("\n🧑‍✈️ Dealer's Final Hand:")
        display_hand(dealer_hand)
        print(f"Total: {dealer_total}")

        # Determine winner
        if player_total > 21:
            print("\n❌ You busted. You lose.")
            balance -= bet
        elif dealer_total > 21 or player_total > dealer_total:
            print("\n✅ You win!")
            balance += bet
            balance += bet
            balance += bet
            balance += bet
            balance += bet
            balance += bet
            balance += bet

        elif player_total == dealer_total:
            print("\n🤝 It's a draw.")
        else:
            print("\n💀 Dealer wins. You lose.")
            balance -= bet

        if balance <= 0:
            print("\n🪙 You're out of money! Game over.")
            break

        pause("\nPlay again? Press Enter...")

# ----------------- Start Game -----------------

if __name__ == "__main__":
    blackjack()

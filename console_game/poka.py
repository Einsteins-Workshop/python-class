import random
import time
from collections import Counter

# ASCII card visuals
CARD_TEMPLATE = """\
┌─────────┐
│{rank:<2}       │
│         │
│    {suit}    │
│         │
│       {rank:>2}│
└─────────┘
"""

SUIT_SYMBOLS = {
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣',
    'Spades': '♠'
}

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANK_VALUES = {rank: i for i, rank in enumerate(RANKS, 2)}

# Card and display logic
def card_to_str(card):
    rank, suit = card
    return CARD_TEMPLATE.format(rank=rank, suit=SUIT_SYMBOLS[suit])

def display_hand(cards):
    lines = ['' for _ in range(7)]
    for card in cards:
        card_lines = card_to_str(card).split('\n')
        for i in range(7):
            lines[i] += card_lines[i] + '  '
    return '\n'.join(lines)

def create_deck():
    return [(rank, suit) for suit in SUITS for rank in RANKS]

def shuffle_deck(deck):
    random.shuffle(deck)

def get_rank_counts(cards):
    return Counter(rank for rank, _ in cards)

def evaluate_hand(cards):
    rank_counts = get_rank_counts(cards)
    counts = sorted(rank_counts.values(), reverse=True)
    if counts[0] == 4:
        return (7, "Four of a Kind")
    elif counts[0] == 3 and counts[1] >= 2:
        return (6, "Full House")
    elif counts[0] == 3:
        return (3, "Three of a Kind")
    elif counts[0] == 2 and counts[1] == 2:
        return (2, "Two Pair")
    elif counts[0] == 2:
        return (1, "One Pair")
    else:
        return (0, "High Card")

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 100
        self.hand = []
        self.active = True
        self.bet = 0

# Betting system
def betting_round(players, pot, phase):
    print(f"\n=== {phase} Betting Round ===")
    time.sleep(1)
    current_bet = 0
    for p in players:
        p.bet = 0

    while True:
        all_called = True
        for player in players:
            if not player.active:
                continue
            print(f"\n{player.name}'s turn (Chips: ${player.chips})")
            print(f"Current bet to call: ${current_bet}")
            print(display_hand(player.hand))
            time.sleep(0.5)
            action = input("Choose action [call/raise/fold]: ").strip().lower()
            if action == "fold":
                player.active = False
            elif action == "raise":
                amount = int(input("Enter raise amount: "))
                total_bet = current_bet + amount
                amount = min(player.chips, total_bet)
                player.chips -= amount
                player.bet = amount
                current_bet = amount
                all_called = False
            elif action == "call":
                call_amount = current_bet - player.bet
                call_amount = min(player.chips, call_amount)
                player.chips -= call_amount
                player.bet += call_amount
            else:
                print("Invalid action.")
                all_called = False
        if all(p.bet == current_bet or not p.active for p in players):
            break

    pot += sum(p.bet for p in players)
    return pot

def showdown(players, community):
    actives = [p for p in players if p.active]
    if len(actives) == 1:
        return actives[0], "Everyone else folded"

    scores = []
    for p in actives:
        combined = p.hand + community
        score, name = evaluate_hand(combined)
        scores.append((score, p, name))

    scores.sort(reverse=True, key=lambda x: x[0])
    if len(scores) > 1 and scores[0][0] == scores[1][0]:
        return None, "Tie"
    return scores[0][1], scores[0][2]

# Game flow
def play_game():
    deck = create_deck()
    shuffle_deck(deck)

    player1 = Player("Player 1")
    player2 = Player("Player 2")
    players = [player1, player2]

    # Deal hole cards
    print("\nDealing hole cards...")
    for p in players:
        time.sleep(1)
        p.hand = [deck.pop(), deck.pop()]
        print(f"{p.name}'s cards:")
        print(display_hand(p.hand))
        print()

    pot = 0
    pot = betting_round(players, pot, "Pre-Flop")

    # Flop
    flop = [deck.pop() for _ in range(3)]
    print("\nDealing Flop...")
    time.sleep(1)
    print(display_hand(flop))
    pot = betting_round(players, pot, "Flop")

    # Turn
    turn = deck.pop()
    print("\nDealing Turn...")
    time.sleep(1)
    print(display_hand(flop + [turn]))
    pot = betting_round(players, pot, "Turn")

    # River
    river = deck.pop()
    community = flop + [turn, river]
    print("\nDealing River...")
    time.sleep(1)
    print(display_hand(community))
    pot = betting_round(players, pot, "River")

    # Showdown
    print("\n=== Showdown ===")
    time.sleep(1)
    for p in players:
        if p.active:
            print(f"{p.name}'s Hand:")
            print(display_hand(p.hand))
            time.sleep(1)

    winner, result = showdown(players, community)
    if winner:
        print(f"\n🏆 {winner.name} wins the pot of ${pot} with {result}")
        winner.chips += pot
    else:
        print(f"\n🤝 It's a tie! Pot is split.")
        for p in players:
            if p.active:
                p.chips += pot // len(players)

    # Final results
    print("\n--- Final Chip Counts ---")
    for p in players:
        print(f"{p.name}: ${p.chips}")

# Run the game
if __name__ == "__main__":
    play_game()
def play_game():
    deck = create_deck()
    shuffle_deck(deck)

    player1 = Player("Player 1")
    player2 = Player("Player 2")
    players = [player1, player2]

    # Deal hole cards
    print("\nDealing hole cards...")
    for p in players:
        time.sleep(1)
        p.hand = [deck.pop(), deck.pop()]
        print(f"{p.name}'s cards:")
        print(display_hand(p.hand))
        print()

    pot = 0
    pot = betting_round(players, pot, "Pre-Flop")

    # ✅ FIX: Check if only one player remains
    active_players = [p for p in players if p.active]
    if len(active_players) == 1:
        winner = active_players[0]
        print(f"\n🏆 {winner.name} wins the pot of ${pot} (everyone else folded)")
        winner.chips += pot
        return

    # Flop
    flop = [deck.pop() for _ in range(3)]
    print("\nDealing Flop...")
    time.sleep(1)
    print(display_hand(flop))
    pot = betting_round(players, pot, "Flop")
    active_players = [p for p in players if p.active]
    if len(active_players) == 1:
        winner = active_players[0]
        print(f"\n🏆 {winner.name} wins the pot of ${pot} (everyone else folded)")
        winner.chips += pot
        return

    # Turn
    turn = deck.pop()
    print("\nDealing Turn...")
    time.sleep(1)
    print(display_hand(flop + [turn]))
    pot = betting_round(players, pot, "Turn")
    active_players = [p for p in players if p.active]
    if len(active_players) == 1:
        winner = active_players[0]
        print(f"\n🏆 {winner.name} wins the pot of ${pot} (everyone else folded)")
        winner.chips += pot
        return

    # River
    river = deck.pop()
    community = flop + [turn, river]
    print("\nDealing River...")
    time.sleep(1)
    print(display_hand(community))
    pot = betting_round(players, pot, "River")
    active_players = [p for p in players if p.active]
    if len(active_players) == 1:
        winner = active_players[0]
        print(f"\n🏆 {winner.name} wins the pot of ${pot} (everyone else folded)")
        winner.chips += pot
        return
    elif len(active_players) == 0:
        print(f"\n🤷 Nobody wins. All players folded.")
        return

    # Showdown
    print("\n=== Showdown ===")
    time.sleep(1)
    for p in active_players:
        print(f"{p.name}'s Hand:")
        print(display_hand(p.hand))
        time.sleep(1)

    winner, result = showdown(players, community)
    if winner:
        print(f"\n🏆 {winner.name} wins the pot of ${pot} with {result}")
        winner.chips += pot
    else:
        print(f"\n🤝 It's a tie! Pot is split.")
        for p in active_players:
            p.chips += pot // len(active_players)

    # Final results
    print("\n--- Final Chip Counts ---")
    for p in players:
        print(f"{p.name}: ${p.chips}")


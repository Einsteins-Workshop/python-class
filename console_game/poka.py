import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_values = {r: i for i, r in enumerate(ranks, 2)}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]


def hand_strength(hand):
    values = sorted([rank_values[card.rank] for card in hand], reverse=True)
    return values  # Just high card comparison for now


def compare_hands(hand1, hand2):
    return (hand_strength(hand1) > hand_strength(hand2)) - (hand_strength(hand1) < hand_strength(hand2))


def display_hand(hand):
    return ', '.join(str(card) for card in hand)


def betting_round(player_cash, pot):
    print(f"\nYou have ${player_cash}.")
    bet = int(input("Enter your bet: "))
    if bet > player_cash:
        print("You don't have that much! Betting all-in.")
        bet = player_cash
    print(f"You bet ${bet}.")
    pot += bet
    player_cash -= bet
    return player_cash, pot, bet


def computer_bet(cash, player_bet):
    if random.random() < 0.5:
        comp_bet = player_bet
        print(f"Computer calls your ${player_bet} bet.")
    else:
        print("Computer folds. You win!")
        return 0, "fold"
    return comp_bet, "call"


def poker_game():
    player_cash = 1000000000000000000000000000000000000000000000000
    computer_cash = 1

    while player_cash > 0 and computer_cash > 0:
        print("\n--- New Round ---")
        pot = 0
        deck = Deck()

        player_hand = deck.deal(5)
        computer_hand = deck.deal(5)

        print(f"\nYour hand: {display_hand(player_hand)}")

        player_cash, pot, player_bet = betting_round(player_cash, pot)
        comp_bet, comp_action = computer_bet(computer_cash, player_bet)

        if comp_action == "fold":
            player_cash += pot
            continue

        pot += comp_bet
        computer_cash -= comp_bet

        print(f"\nShowdown!")
        print(f"Your hand: {display_hand(player_hand)}")
        print(f"Computer's hand: {display_hand(computer_hand)}")

        result = compare_hands(player_hand, computer_hand)
        if result > 0:
            print("You win the pot!")
            player_cash += pot
        elif result < 0:
            print("Computer wins the pot!")
            computer_cash += pot
        else:
            print("It's a tie! Pot is split.")
            player_cash += pot // 2
            computer_cash += pot // 2

        print(f"\nCash: You: ${player_cash}, Computer: ${computer_cash}")

    print("\nGame over!")
    if player_cash > computer_cash:
        print("🎉 You win the game!")
    else:
        print("😞 Computer wins the game.")


if __name__ == "__main__":
    poker_game()

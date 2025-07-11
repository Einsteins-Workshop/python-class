
import random

print('WELCOME TO BLACKJACK')

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

# First, create an object that represents a deck of cards.
class Deck:
    def __init__(self):
        # This represents all the discarded cards.
        self._discard = []

        # This represents the draw pile
        self._draw_pile = []

        self.reset()

        pass

    def deal_card(self):
        if len(self._draw_pile) == 0:
            self.reset()

        return self._draw_pile.pop()


        # This function should randomly deal a card from the not already dealt cards and remove it
        # from the draw pile.  It should return the dealt card.

        # Also, determine whether the deck should be reshuffled. This could be when all cards are dealt,
        # or when the cards get below some preset amount (like 10).



    def discard_card(self, card):
        # This function should add a card to the discard pile.
        pass

    def reshuffle(self):
        # Reshuffle the deck by adding the discard pile to the draw pile of cards.
        pass

    def reset(self):
        # Create a list representing the deck of all cards not yet dealt out. This should be a set
        # of values representing a card. The values could be a number from 0 to 51, a string with
        # rank and suit, are a two element tuple with rank and suit. Make sure to save the deck to self._draw_pile
        self._draw_pile = (list(range(52)))
        random.shuffle(self._draw_pile)




def card_name(value):


    if value // 13 == 0:
      suit = "spades"
    elif value // 13 == 1:
      suit = "clubs"
    elif value // 13 == 2:
      suit =  "hearts"
    elif value // 13 == 3:
      suit =  "diamonds"


    rank = blackjack_value(value)

    return(rank + f" of {suit}")




def blackjack_value(value):

    if value % 13 == 0:
        rank = "2"
    elif value % 13 == 1:
        rank = "3"
    elif value % 13 == 2:
        rank = "4"
    elif value % 13 == 3:
        rank = "5"
    elif value % 13 == 4:
        rank = "6"
    elif value % 13 == 5:
        rank = "7"
    elif value % 13 == 6:
        rank = "8"
    elif value % 13 == 7:
        rank = "9"
    elif value % 13 == 8:
        rank = "10"
    elif value % 13 == 9:
        rank = "jack"
    elif value % 13 == 10:
        rank = "queen"
    elif value % 13 == 11:
        rank = "king"
    elif value % 13 == 12:
        rank = "ace"

    return (rank)

def card_score(rank):
    value = rank
    if rank =='jack':
        value = 10
    elif rank == 'queen':
        value = 10

    elif rank == 'king':
        value = 10

    elif rank == 'ace':
        value = 1
    else:
        value = int(rank)
    return value

def total_score(hand):
    aces = 0
    total = 0
    for card in hand:
        value = card_score(blackjack_value(card))
        total = total + value
        if value == 1:
            aces = aces + 1
    if (total < 12) and (aces > 0):
        total = total + 10
    return total


deck_of_cards = Deck()
deck_of_cards.reset()
#for my_card in hand:
##    print(card_name(my_card))
 #   value = blackjack_value(my_card)
#    score = card_score(value)
 #   print(score)

chips = 100
while True:
    print(f"you have {chips}")
    if chips == 0:
        break
    play_again = input('want to play again (y/n)')
    if play_again == "n":
        print('nice job')
        break
    bet = 0
    while (bet <= 0) or (bet > chips):
        bet = int(input('how much do you want to bet'))

    card = deck_of_cards.deal_card()
    card2 = deck_of_cards.deal_card()
    card3 = deck_of_cards.deal_card()
    card4 = deck_of_cards.deal_card()
    dealer_hand = [card , card2]
    your_hand = [card3 , card4]
    print(f'dealers cards hidden , {card_name(card2)}')
    print(f'your cards {card_name(card3)} , {card_name(card4)}')
    print(total_score(your_hand))
    while total_score(your_hand) < 21:
        hit = input('want to hit or stand (h/s)')
        if hit == "h":
            new_card = deck_of_cards.deal_card()
            your_hand.append(new_card)

            print(f'Your hand is: {" ".join([card_name(x) for x in your_hand])}')
            print(total_score(your_hand))
        elif hit == 's':
            break

    end_player_score = total_score(your_hand)
    if end_player_score > 21:
        print(f"you busted with score {total_score(your_hand)}")
        chips = chips - bet
    elif (end_player_score == 21) and len(your_hand) == 2:
        print('you got black jack')
        chips = chips + bet + bet
    else:
        while total_score(dealer_hand) < 17:
            new_card = deck_of_cards.deal_card()
            dealer_hand.append(new_card)
            print(f'dealer hand is: {" ".join([card_name(x) for x in dealer_hand])}')
        end_dealer_score = total_score(dealer_hand)
        if end_dealer_score > 21:
            print(f"the dealer busted with score {end_dealer_score}")
            chips = chips + bet
        elif end_player_score > end_dealer_score:
            print(f"you won")
            print(f"the dealers score was {end_dealer_score}")
            print(f'your score was {end_player_score}' )
            chips = chips + bet
        else:
            print("you lost")
            print(f"the dealers score was {end_dealer_score}")
            print(f'your score was {end_player_score}')
            chips = chips - bet
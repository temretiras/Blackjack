import random
def generate_deck(_suits, _cards):
    random.seed(0)
    n = 0
    deck = [(i, j) for i in _suits for j in _cards]
    random.shuffle(deck)
    while True:
        yield deck[n]
        n += 1
        if n == 52:
            random.shuffle(deck)
            n = 0


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = generate_deck(suits, cards)


def get_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card[1] in ['J', 'Q', 'K']:
            value += 10
        elif card[1] == 'A':
            num_aces += 1
        else:
            value += int(card[1])
    for i in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    return value


def play_blackjack():
    player_hand = []
    dealer_hand = []
    player_hand.append(get_next_card())
    dealer_hand.append(get_next_card())
    player_hand.append(get_next_card())
    dealer_hand.append(get_next_card())
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    print('Player hand:', player_hand, 'Value:', player_value)
    print('Dealer hand:', [dealer_hand[0], ('', '')], 'Value:', dealer_hand[0][1])
    while True:
        if player_value == 21:
            print('Blackjack! Player wins.')
            return
        elif player_value > 21:
            print('Bust! Dealer wins.')
            return
        elif dealer_value > 21:
            print('Dealer busts! Player wins.')
            return
        else:
            choice = input('Hit or stand? ')
            if choice.lower() == 'hit':
                player_hand.append(get_next_card())
                player_value = get_hand_value(player_hand)
                print('Player hand:', player_hand, 'Value:', player_value)
            elif choice.lower() == 'stand':
                while dealer_value < 17:
                    dealer_hand.append(get_next_card())
                    dealer_value = get_hand_value(dealer_hand)
                    print('Dealer hand:', dealer_hand, 'Value:', dealer_value)
                if dealer_value > 21:
                    print('Dealer busts! Player wins.')
                    return
                elif dealer_value > player_value:
                    print('Dealer wins!')
                    return
                elif player_value > dealer_value:
                    print('Player wins!')
                    return
                else:
                    print('It\'s a tie!')
                    return


def get_next_card():
    return next(deck)


play_blackjack()

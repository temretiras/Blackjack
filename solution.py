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
shuffled_deck = generate_deck(suits, cards)


def get_next_card():
    return next(shuffled_deck)


# DO NOT EDIT ABOVE THIS LINE
# BELOW THIS LINE WILL BE YOUR SOLUTION

colors = {'Spades': 'black', 'Hearts': 'red', 'Diamonds': 'red', 'Clubs': 'black'}

def get_hand_sum(hand):
    sum = 0
    num_K = 0
    for card in hand:
        if card[1] in ['J', 'Q', 'A']:
            sum += 10
        elif card[1] == 'K':
            if colors[card[0]] == 'black':
                sum += 11
            else:
                sum += 1
            num_K += 1
        else: 
            sum += int(card[1])
    return sum  
  
def playBlackjack():
    sage_money = int(input("Sage's money: "))
    num_games = int(input("Number of games: "))
    for game in range(num_games):
        print(f"Game {game+1}")        
        sage_hand = []
        king_hand = []
        sage_hand.append(get_next_card())
        sage_hand.append(get_next_card())
        king_hand.append(get_next_card())
        king_hand.append(get_next_card())
        sage_value = get_hand_sum(sage_hand)
        king_value = get_hand_sum(king_hand)
        old_king_value = get_hand_sum([king_hand[1]])
        print("King’s cards: (*)"+ str(king_hand[1])) 
        print("Total value:", old_king_value)   
        print("Sage's cards: " + str(sage_hand[0]) + str(sage_hand[1]))   
        print("Total value:", sage_value)   
        while True:
            if sage_value == 21:
                print('It is Blackking! You won!')
                sage_money = sage_money + 50
                break
            elif sage_value > 21:
                print('You busted! You lost!')
                sage_money = sage_money - 50
                break
            elif king_value > 21:
                print("King busted! You won!")
                sage_money = sage_money + 50
                break
            else:
                HorS = input("Do you want to hit or stand? [H/S] ").lower()
                if HorS == "h":
                    sage_hand.append(get_next_card())
                    sage_value = get_hand_sum(sage_hand)
                    print("Sage's cards: ", end="")
                    for element in sage_hand:
                        print(element, end="")
                    print()
                    print("Total value:", sage_value) 
                elif HorS == "s":
                    print("King's cards: ", end="")
                    for element in king_hand:
                        print(element, end="")
                    print()
                    print("Total value:", king_value)
                    while king_value < 17:
                        king_hand.append(get_next_card())
                        king_value = get_hand_sum(king_hand)
                        print("King's cards: ", end="")
                        for element in king_hand:
                            print(element, end="")
                        print()
                        print("Total value:", king_value)   
                    if king_value > 21:
                        print("King busted! You won!")
                        sage_money = sage_money + 50
                        break
                    elif king_value > sage_value:
                        print('King has higher value. You lost!')
                        sage_money = sage_money - 50
                        break
                    elif sage_value > king_value:
                        print("You have higher value. You won!")
                        sage_money = sage_money + 50
                        break
                    else:
                        print('It\'s a tie!')
                        break
    print(f"Final money is {sage_money}")
playBlackjack()
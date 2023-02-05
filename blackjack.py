import random
#creating global variables
playing = True
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace': 11}



#creating card class
class Card():
    """docstring for deck"""
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit 
        self.value = values[self.rank]


    def __str__(self):
       return f'card {self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        #empty list to make cards
        
        self.all_cards = []
        #for loop to appened the card objects
        for suit in suits:
            for rank in ranks:
                dummy_card = Card(suit,rank)
                self.all_cards.append(dummy_card)
                #print(dummy_card)  #to check wheater loop is working

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp
        

    def remove_card(self):
        removed_card = self.all_cards.pop(0)
        return removed_card
        
        
class Hand:
    """docstring for Hand"""
    def __init__(self):
        self.cards = []  # starting with an empty list to later append cards
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces


    def add_card(self,card):
        self.cards.append(card)
        print(card)
        self.value += values[card.rank]
        if card.suit == 'Ace':
            self.aces += 1
        


    def ace_value_check(self):
        if self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10


class Chip:
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):

        self.total += self.bet 


    def lose_bet(self):

        self.total -= self.bet 

#repetitive funstions
def take_bet(self):
    while True:
        
        try:
            
            bet = int(input('Please enter your bet till 100 :'))

        except ValueError:#checks for an error
            print('Please enter a number!')
        if int(bet) > self.total:
            print('the number must be within range of 100!')
        else:
            break



        

def hit(deck,hand):
    
    hand.add_card(deck.remove_card())
    hand.ace_value_check()

def hit_or_stand(deck,hand): # asks to hit or stand
    global playing  # to control an upcoming while loop
    while playing:
        global hit_stand
        hit_stand = input('Enter "hit" or "stand" : ' )
        if hit_stand.lower() == 'hit':
            hit(deck,hand)
            playing= False
            break
        elif hit_stand.lower()== 'stand':
            print("dealer plays player stands")
            playing = False
            break
        else:
            print('please enter a h or a s!')
def show_some(player,dealer):
    print(f'player cards:\n',*player.cards, sep ='\n' )
    print('\n dealer cards:')
    print('\n< Hidden Card >')
    print(dealer.cards[1])

def show_all(player,dealer):
    print(f"dealers cards : \n", *dealer.cards ,sep = '\n')
    print(f"\ntotal value of dealers cards : {dealer.value}")
    print(f"players cards :  \n", *player.cards ,sep = '\n')
    print(f"\ntotal value of players cards : {player.value}")

# different win scenarios
def player_busts(player,dealer,chips):
        print('Oops! YOU BUSTED! try again...')
        chips.lose_bet()
    
def player_wins(player,dealer,chips):
        print('YOU WIN! ')
        chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('YOU WIN! ')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('Oops! YOU BUSTED! try again...')
    chips.lose_bet()
    
def push(player,dealer):
    print("IT'S A TIE...")
    


   
while True:#main loop
    

    print("Welcome to the world of casino!")
    #creation of instances
    prac = Deck()
    prac.shuffle()
    Player_hand = Hand()
    dealer_hand = Hand()
        
    Player_hand.add_card(prac.remove_card()),Player_hand.add_card(prac.remove_card())
    
    dealer_hand.add_card(prac.remove_card()),dealer_hand.add_card(prac.remove_card())


    player_chips = Chip()

    take_bet(player_chips)
    show_some(Player_hand,dealer_hand)
    # sub main war loop 
    while playing:
        hit_or_stand(prac,Player_hand) 
        
    if Player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(prac,dealer_hand)
            
            
    if Player_hand.value <= 21:
        player_wins(Player_hand,dealer_hand,player_chips)
        #show_all(Player_hand,dealer_hand)
        playing = False
    elif dealer_hand.value >= 17:
        dealer_wins(Player_hand,dealer_hand,player_chips)
        #show_all(Player_hand,dealer_hand)
        playing = False
    elif Player_hand.value < 21: # checks for a player win 
        player_busts(Player_hand,dealer_hand,player_chips)
        
        playing = False
    elif dealer_hand.value < 17:
        dealer_busts(Player_hand,dealer_hand,player_chips)
        
        playing = False
    else:
        push(Player_hand,dealer_hand)
    print(f'your total chips are :{player_chips.total}')
    show_all(Player_hand,dealer_hand)
    new_game = input('DO you want to play again ? (Y/N) :')#asks for a replay 
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break


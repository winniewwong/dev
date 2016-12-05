# Mini-project #6 - Blackjack
http://www.codeskulptor.org/#user38_0ZH6wMjbgIPJGeh.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

deck = []
dealer_hand = []
player_hand = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])           
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    
# define hand class
class Hand:
    def __init__(self):
        # create Hand object to empty list
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        hand_string = ""
        
        for card in self.cards:
           hand_string += card.suit            
           hand_string += card.rank
           hand_string += ' ' 
        
        hand_string = "Hand contains " + hand_string             
        return hand_string    
            

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append( card )

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        
        # Is Aces exists?
        hasAces = False
        
        # sum of card values with Aces as 1
        for card in self.cards:
           if card.rank in RANKS:
               hand_value += VALUES[ card.rank ]
               if card.rank == 'A':
                    hasAces = True
     
        if hasAces == True:
            if ( hand_value + 10 ) <= 21:
                hand_value += 10
               
        return hand_value         
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            card.draw( canvas, pos )
          
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        
        for suit in SUITS: 
           for rank in RANKS:
              # create a Card object using Card(suit, rank)
              card = Card(suit, rank)
                
              # add the card to the card list for the deck
              self.deck.append( card )
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle( self.deck )
       
    def deal_card(self):
        # deal a card object from the deck
        # deal_card will return the last card of the deck
        card = self.deck.pop()
        return card
    
    def __str__(self):
        # return a string representing the deck
        deck_string = ""
        
        for card in self.deck:
           deck_string += card.suit            
           deck_string += card.rank
           deck_string += ' ' 
        
        deck_string = "Deck contains " + deck_string             
        return deck_string 

#define event handlers for buttons
def deal():
    global outcome, score, in_play, deck, dealer_hand, player_hand

    # if the "Deal" button is clicked during the middle of a round
    # the program reports that the player lost the round
    if in_play:
       score -= 1
        
    # Create and shuffle a new deck
    deck = Deck()
    print deck
    deck.shuffle()
    print deck
    
    # deals the two cards to both the dealer and the player
    dealer_hand = Hand()
    player_hand = Hand()
   
    dealer_hand.add_card( deck.deal_card() )    
    player_hand.add_card( deck.deal_card() )   
    dealer_hand.add_card( deck.deal_card() )   
    player_hand.add_card( deck.deal_card() )
    
    # start the blackjack
    in_play = True
    outcome = ""
    
    print "dealer's", dealer_hand
    print "player's", player_hand
    print "dealer's hand value =", dealer_hand.get_value()
    print "player's hand value =", player_hand.get_value()

def hit():
    global outcome, in_play, score, dealer_hand, player_hand

    # if the hand is in play, hit the player
    if in_play == True:
        # if the value of the player hand is less than or equal to 21, add extra card to player's hand
        if player_hand.get_value() <= 21:
           player_hand.add_card(deck.deal_card())
          
           # if busted(value exceeds 21), assign a message to outcome, update in_play and score
           if player_hand.get_value() > 21:
              # stop the blackjack  
              in_play = False
              outcome = "You went bust and lose."    
              score -= 1
                            
        print "dealer's", dealer_hand
        print "player's", player_hand
        print "dealer's hand value = ", dealer_hand.get_value()
        print "player's hand value = ", player_hand.get_value()
        print "score", score
        print outcome
    
def stand(): 
    global outcome, in_play, score, dealer_hand, player_hand

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:       
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card( deck.deal_card() )
   
        # assign a message to outcome, update in_play and score
        in_play = False
    
        if dealer_hand.get_value() > 21:
            outcome = "Dealer have busted."
            score += 1
        elif player_hand.get_value() <= dealer_hand.get_value():
            outcome = "You lose."
            score -= 1
        else:
            outcome = "You win."
            score += 1
        
        print "dealer", dealer_hand
        print "player", player_hand
        print "dealer's hand value = ", dealer_hand.get_value()
        print "player's hand value = ", player_hand.get_value()
        print "score", score
        print outcome
            
# draw handler    
def draw(canvas):
    # Dealer's hand
    count = 0
    for card in dealer_hand.cards:
        if in_play and count == 0:
            card.draw_back(canvas, [80, 250])
        else:
            card.draw(canvas, [80 + 100 * count , 250])
       
        count += 1
    
    # Player's hand
    count = 0
    for card in player_hand.cards:
        card.draw(canvas, [80 + 100 * count , 450])
        count += 1   
        
    # Blackjack label
    canvas.draw_text("Blackjack", (100, 100), 40, 'Cyan') 
   
    # Dealer label
    canvas.draw_text("Dealer", (80, 200), 30, 'Black') 
  
    # display dealer's hand value if not playing
    if in_play == False:
       canvas.draw_text("Hand value " + str(dealer_hand.get_value()), (80, 230), 30, 'Black') 
      
    # Player label
    canvas.draw_text("Player", (80, 400), 30, 'Black') 
    
    # Player's hand value 
    canvas.draw_text("Hand value " + str(player_hand.get_value()), (80, 430), 30, 'Black') 
      
    # update outcome
    canvas.draw_text(outcome, (300, 200), 30, 'Red')

    # update score
    canvas.draw_text("Score " + str(score), (400, 100), 30, 'Black')

    # display "New deal?" message to the player
    message = ""
    if in_play == False:
        message = "New deal?"
    else:
        message = "Hit or stand?"
   
    canvas.draw_text(message, (200, 400), 30, 'Red')
  

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric

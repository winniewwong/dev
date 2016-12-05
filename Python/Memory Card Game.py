# implementation of card game - Memory
http://www.codeskulptor.org/#user38_K5NeL2mz2dpz6QD.py

import simplegui
import random

cards = []
indices = []
turn_counter = 0

# helper function to initialize globals
def new_game():   
    global cards, indices, turn_counter
  
    # create 16 cards, each card number ranges from 0 to 7 and appears twice and exposed state
    # first element of the list stores the card number
    # second element of the list stores the exposed state, face up(True) or face down(False)
    cards = []
    for num in range(8):
      cards.append( [ num, False ] )
      cards.append( [ num, False ] )
   
    # shuffle the cards
    random.shuffle(cards)
    
    #print cards
    
    # reset last two exposed cards indices to empty list. Maximum size of the list is 2
    indices = []
    
    # reset turn counter to 0
    turn_counter = 0

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards, indices, turn_counter
    
    # convert the pos in tuple to list
    p = list(pos)
         
    # get the index of the current exposed from the position
    index = p[ 0 ] // ( 800 / len( cards ) )
   
    #print "index", index   
    #print cards
    #print indices
    
    # ignore the mouseclick if the selected card have already been exposed
    if cards[ index ][ 1 ] == True:
        return
  
    # check if the last two exposed cards match or not
    if ( len(indices) == 2 ):
        #print "indices[ 0 ]", cards[ indices[ 0 ] ]
        #print "indices[ 1 ]", cards[ indices[ 1 ] ]
       
        # clear indices of the last two exposed cards
        if ( cards[ indices[ 0 ] ] == cards[indices[ 1 ] ] ):       
           indices = []
           #print "clear indices", indices
        # unflip the last two exposed cards if not match
        else:        
           cards[indices[ 0 ]][ 1 ] = False
           cards[indices[ 1 ]][ 1 ] = False
           indices = []
           #print "clear indices", indices          
     
    # flip the current exposed card 
    cards[ index ][ 1 ] = True
                 
    # keep track of the indices of two cards that were most recently clicked 
    indices.append( index );
    #print "indices", indices
    
    # increment counter for the first card selected during a turn
    if len( indices ) == 1:
        turn_counter += 1
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards
    
    # draw polygon
    for i in range( 16 ):
       point_list = [ [800 / 16 * i, 0 ], [ 800 / 16 * ( i + 1 ), 0], [ 800 / 16 * ( i + 1 ), 100 ], [ 800 / 16 * i, 100 ] ]
       # Black background if face up
       if cards[ i ][ 1 ] == True:
          canvas.draw_polygon( point_list, 5, "Gray", "Black" )
       # Green background if face down
       else:
          canvas.draw_polygon( point_list, 5, "Gray", "Green" )
    
    # draw the value of the cards
    if len( cards ) > 0:          
       pos = [ ( 800 / len( cards ) / 2 ) - 10, 70 ]
       for c in cards: 
          if c[ 1 ] == True:
             canvas.draw_text( str( c[ 0 ] ), pos, 50, "White" )   
          
          pos[ 0 ] += 800 / len( cards )

    # update turn counter
    label.set_text( str( turn_counter ) );
                
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

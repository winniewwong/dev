# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
http://www.codeskulptor.org/#user38_r0YohKOcZojFDeo.py

#Guess a number using binary search

import simplegui
import random
import math

# intialize globals
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables
    global secret_number
    global num_guess
    global max_guess
    
    """ Reset number of guess """
    num_guess = 0  
    
    """ max guess = 2**n >= high - low + 1 """
    """ Maximum number of guess is 7 for range 0 to 99 """  
    """ Maximum number of guess is 10 for range 0 to 999 """     
    max_guess = int(math.ceil( math.log( num_range, 2 ) ) )
   
    if num_range == 1000:   
        """ Secret number range 0 to 999 """
        secret_number = random.randrange( 0, 1000 )     
    else:    
        """ Secret number range 0 to 99 """
        secret_number = random.randrange( 0, 100 )
    
    """ blank line """
    print ""
    
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", max_guess
   
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
        
    num_range = 100
      
    new_game()
       
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
       
    num_range = 1000
       
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global input_guess
    global num_guess
    global max_guess
    
    """ Convert the input string guess to an integer """
    input_guess = int(guess)
    
    num_guess += 1
    
    """ blank line """
    print ""
    
    print "Guess was", input_guess        
   
    print "Number of remaining guesses is", max_guess - num_guess
    
    if input_guess == secret_number:
        print "Correct!"
        new_game()
    elif input_guess < secret_number:            
        if num_guess >= max_guess:
            print "You ran out of guesses. The number was", secret_number
            new_game()
        else:
            print "Higher!"
    else:   
        if num_guess >= max_guess:
            print "You ran out of guesses. The number was", secret_number
            new_game()
        else:
            print "Lower!"
    
# create frame
f = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric

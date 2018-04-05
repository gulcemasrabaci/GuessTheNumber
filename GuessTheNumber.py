import simplegui
import random
import math

num_range_max = 100

# helper function to start and restart the game
def new_game():
    """Starts or restarts game, sets the global variables"""
    global guesses_left
    guesses_left = int(math.ceil(math.log(num_range_max, 2)))
    
    global secret_number
    secret_number = random.randrange(0, num_range_max)
    
    print "Game begins!" 
    print "Range is [0, " + str(num_range_max) + ")" 
    print "Number of remaining guesses is", guesses_left
    print

# define event handlers for control panel
def range100():
    """button that changes the range to [0,100) and starts a new game""" 
    global num_range_max 
    num_range_max = 100
    new_game()

def range1000():
    """button that changes the range to [0,1000) and starts a new game"""     
    global num_range_max
    num_range_max = 1000
    new_game()
    
def input_guess(guess):
    """the input handler that plays the game and prints out the result"""
    int_guess = int(guess)
    print "Your guess was", int_guess
    
    global guesses_left
    guesses_left -= 1
    
    if not 0 <= int_guess < num_range_max:
        print "You are out of range! Try again."
        print
        new_game()
    elif int_guess == secret_number:
        print "Correct!"
        print
        new_game()
    else:
        print "Number of remaining guesses is", guesses_left
        if guesses_left == 0:
            print "You ran out of guesses. Correct answer was", secret_number
            print
            new_game()
        elif int_guess > secret_number:
            print "Lower"
            print
        else:
            print "Higher"
            print
            
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Enter a guess!", input_guess, 100)                              
frame.add_button("Range is [0, 100)", range100)
frame.add_button("Range is [0, 1000)", range1000)
frame.start()

# call new_game 
new_game()

#Garrett Fuller
#Tic-Tac-Toe game



import time
import random
random.seed()


###########################################################################
# GLOBAL VARIABLE ASSIGNMENT
###########################################################################


board = {'1a':' ', '1b':' ', '1c':' ', '2a':' ', '2b':' ', '2c':' ',
             '3a':' ', '3b':' ', '3c':' '}
"""Stores the state of the board for display"""

availableMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
"""Used moves are removed from this list as they are made, so I don't have to
 read the dictionary every time a move is calculated.
"""


winConditions = [('1a','1b','1c'),('2a','2b','2c'), ('3a','3b','3c'), ('1a','2a','3a'),
       ('1b','2b','3b'), ('1c','2c','3c'),('1a','2b','3c'), ('3a','2b','1c')]
"""This is a list of three tuples of all the win conditions. Used to check first
 for winning moves, and second for blocking moves.
"""


firstMoves =['1a','1c','3a','3c']
"""The four corners are the best opening moves for the computer. This list
 depopulates as the moves are used like leagalMoves.
"""

# commented out for refactoring of game cycle
"""def flip_for_turn():
    uses random choice to choose between h or t and prints the result to screen"
    #call it in the air? Funny statement if user waits too long.

    time.sleep(.5)
    print('\n\tLet\'s flip a coin to see who goes first')
    called = str(input("\n\tHeads or tails? h or t: ")).lower()
    coin = random.choice('h' 't')

    time.sleep(.5)
    if coin == 'h':
        print("\n\tThe coin landed on heads.")
    else:
        print("\n\tThe coin landed on tails.")
    time.sleep(.5)

    if called == coin:
        print("\n\tYou are going first.")
        turn = 'human'
    else:
        print("\n\tBad luck. \n\tThe computer goes first.")
        turn = 'computer'
    time.sleep(.5)

    return(turn)"""


def draw_grid():
    """ Draws the game board. Calls draw_row() and passes count which acts as row number."""
    time.sleep(.5)
    count = 0

    while count < 3:
        count+=1
        draw_row(count)

        if count <=2:
            print("\t  ==|===|==")
    time.sleep(.5)


def draw_row(row_index):
    """ Takes an arguement called row from drawGrid (count)
    Draws the rows and grid lables. Builds the strings to print with .format
    calling board.
    """

    if row_index == 1:
        print("\n\t  a   b   c")

    #cast index number to a string for evaluation as a location
    row_number = str(row_index)

    print("\t{} {} | {} | {}".format(row_number, board[row_number +'a'],
                                     board[row_number +'b'], board[row_number +'c']))


def check_move(move):
    """checks to see if a move is legal. Takes move string as parameter.
    Returns Boolean"""
    if move not in availableMoves:
        time.sleep(.5)
        print('\n\n\tThat is not a legal move.\n')
        return(False)
    else:
        return(True)


def remove_move(move):
    """remove_move will always be called after the legality of a move has been
    checked. It takes move as a parameter then removes the move from available
    moves and from first move"""
    availableMoves.remove(move)

    if move in firstMoves:
        if move in firstMoves:
            firstMoves.remove(move)


def update_board(move, piece):
    """Takes move, a string '1a' and piece 'X' or 'O' from main. Updates the
    game board and calls remove_move to depopulate used moves.
    """
    remove_move(move)
    board[move] = piece


def initialize_game():
    """Initializes the state of the game."""

    for spot in board:
        board[spot] = ' '
    availableMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
    firstMoves =['1a','1c','3a','3c']

    return (availableMoves,firstMoves)

def play_again():
    """Asks the uses if they want to play again. This set of functions could use
    some cleaning.
    """

    print("\n\tWould you like to play again? :)")
    again = str(input("\n\ty or n: ")).lower()

    return(again)


def get_move():

###########################################################################
# |=========================|| MAIN ||=========================|
###########################################################################

def main():


    print('\n\tWelcome to tic-tac-toe!.')
    #mock up of pygame thing. Broken and wrong.
    """ interface = str(input('Would you like to play in pygame? y or n'))
    if interface == 'y':
        pytictac.main()
        break"""

    #commented out for refactoring of game cycle
    #first_turn = flip_for_turn()
    print("This is a version for two human players.")
    print('\n\tHere is the game board.')
    draw_grid()

    turn_count = 1
    victory = False

    next_piece = {'X' : 'O', 'O' : 'X'}
    game_piece = 'O'

    while victory == False:


        #Get a move
        #Check if legal
        #Update board
        #draw board
        #check win

        victory = True

if __name__ == "__main__":
    """must use C-u C-c C-c to run in e-macs. Something complex going on here"""
    main()

    again = 'none'

    while again != 'n':
        availableMoves,firstMoves = initialize_game()
        again = play_again()
        if again == 'y':
            main()

    print("\n\tThanks a whole lot for playing!")

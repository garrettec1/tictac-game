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


def flip_for_turn():
    """uses random choice to choose between h or t and prints the result to screen"""
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

    return(turn)


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

# I think that isolating the input code is good. But it seems a bit
# strange to also have this modify the availableMoves list, and check
# whether it's a valid move.  I would probably put this into a
# separate function that actually makes a move. Then the updating the
# board and the updating of the legal move step are tied together.
# This is appropriate since they are actualy just different views of
# the same data. Having them updated at different points in the code
# and by different functions means that it would be much easier for
# them to get out of sync. Same for firstMoves
def get_human_move():
    """Gets input from player, loops over check_move till that returns true.
    Returns the Human Move as a string: eg. '1a'
    """

    legal_move = False
    time.sleep(.5)
    print("\n\tIt is your turn to move.")
    time.sleep(.5)

    while (not legal_move):
        moving = str(input("\n\tEnter your move. eg. 1a or 3c: "))
        move = moving.lower()
        legal_move = check_move(move)

    return(move)


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
    """do_move will always be called after the legality of a move has been
    checked. It takes move as a parameter then removes the move from available
    moves and from first move"""
    availableMoves.remove(move)

    if move in firstMoves:
        if move in firstMoves:
            firstMoves.remove(move)


def computer_move(turn):
    """ Takes the turn_count variable from main as turn.
    The first if and elif handle the first two computer moves in the game.
    calc_move handles all other moves. Returns move as a string. eg: '1a'
    """
    time.sleep(.5)
    print("\n\tIt is the computer turn.")

    #only takes from first move when is goes first? have to revisit this.
    if turn == 1:
        move = random.choice(firstMoves)
    elif turn == 3:
        move = random.choice(firstMoves)
    else:
        move = calc_move()

    return(move)


def calc_move():
    """ Calls winBlock twice. First to find the winning move as the computer, if that
    does not return a valid move, it finds a move to block a winning move.
    If there are no winning moves or moves to be blocked. The computer takes the
    remaining corner.
    """

    move = win_block('X')

    if move not in availableMoves:
        move = win_block('O')

        if move not in availableMoves:
            move = random.choice(firstMoves)

    return(move)


def win_block(piece):
    """ Takes piece passed from calcMove, a string 'X' or 'O'. move is assigned zero
    so that if a valid move is not found, win_block returns an invalid move.
    Uses a for loop to pull 3 tuples of win conditions from winConditions[] then a for loop to
    check the state of each location. It returns the location of the empty space.
    """

    move = 0

    for three_in_a_row in winConditions:
        empty = 0
        counter = 0
        for square in three_in_a_row:
            if board[square] == piece:
                counter+=1

            if board[square] == ' ':
                empty = square

            if counter == 2 and empty != ' ':
                move = empty

            if move in availableMoves:
                break

    return(move)


def ftw(piece):
    """ (For The Win) Takes piece from main. A string 'X' or 'O'
    Structured like win_block() with two for loops. Returns victory Bool as True if
    the game has been won.
    """

    victory = False

    for set in winConditions:
        counter = 0
        for squares in set:
            if board[squares] == piece:
                counter += 1

            if counter == 3:
                victory = True
                break

    return(victory)


def update_board(move, piece):
    """Takes move, a string '1a' and piece from main. I mostly made this a function
    because update_board() is more readable
    """
    remove_move(move)
    board[move] = piece


def initialize_game():
    """Initializes the state of the game."""

    # Typically the looping variable (i.e. spots in this case) is a
    # word in singular form. Because it's actually not multiple spots,
    # it's just one.
    for spots in board:
        board[spots] = ' '
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

    # Using the string 'first' as the return value here is sort of an
    # awkward interface. It's inherently ambiguous as to what it
    # means.  Who goes first? Computer or human? The point is you have
    # to KNOW what flip_for_turn means which probably means looking at the
    # code.  How could you do it less ambiguously? Ideally the only
    # thing you have to know about a function is *what* it returns,
    # not how it derived that information.
    first_turn = flip_for_turn()

    print('\n\tHere is the game board.')
    draw_grid()

    if first_turn == 'human':
        human_piece = 'X'
        comp_piece = 'O'
    else:
        human_piece = 'O'
        comp_piece = 'X'

    turn_count = 1
    victory = False

    # The mess of conditionals inside here is kind of intense. It
    # looks like it just evolved into the current state through trial
    # any error (not shocking ;).  But it's level of clarity has
    # become low.  The usage of the gaming variable seems REALLY all
    # over the place.  It's confusing that it gets incremented
    # multiple times throughout this while loop
    while turn_count<10:

        # This was confusing to read.  The words mislead you into
        # thinking this means "when it's not the first turn".  But
        # that's not what it means at all. It actually means, "if the
        # computer is going first."  So it should probably say that ;)
        if first_turn == 'computer':
            move = computer_move(turn_count)
            update_board(move, comp_piece)
            draw_grid()
            turn_count+=1

        if turn_count > 4:
            if ftw(comp_piece):
                time.sleep(2.5)
                print("\n\tThe ",comp_piece,"'s have won the game!")
                break

        if turn_count == 10:
            time.sleep(.5)
            print("\n\tIt's a TIE!")
            break

        move = get_human_move()
        update_board(move, human_piece)
        draw_grid()
        turn_count += 1

        if turn_count > 5:
            if ftw(human_piece):
                time.sleep(2.5)
                print("\n\tThe ",human_piece,"'s have won the game!")
                break

        if turn_count == 10:
            time.sleep(1)
            print("\n\tIt's a TIE!")
            break

        turn = 'none'

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

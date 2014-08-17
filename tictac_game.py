#Garrett Fuller
#Tic-Tac-Toe game



import time
import random
random.seed()
import pytictac


###########################################################################
# GLOBAL VARIABLE ASSIGNMENT
###########################################################################

boardInfo = {'1a':' ', '1b':' ', '1c':' ', '2a':' ', '2b':' ', '2c':' ',
             '3a':' ', '3b':' ', '3c':' '}
"""Stores the state of the board for display"""

legalMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
"""Used moves are removed from this list as they are made, so I don't have to
 read the dictionary every time a move is calculated.
"""

win = [('1a','1b','1c'),('2a','2b','2c'), ('3a','3b','3c'), ('1a','2a','3a'),
       ('1b','2b','3b'), ('1c','2c','3c'),('1a','2b','3c'), ('3a','2b','1c')]
"""This is a list of three tuples of all the win conditions. Used to check first
 for winning moves, and second for blocking moves.
"""

firstMoves =['1a','1c','3a','3c']
"""The four corners are the best opening moves for the computer. This list
 depopulates as the moves are used like leagalMoves.
"""


def coin_flip():
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
        turn = 'first'
    else:
        print("\n\tBad luck. \n\tThe computer goes first.")
        turn = 'second'
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


def draw_row(row):
    """ Takes an arguement called row from drawGrid (count)
    Draws the rows and grid lables. Builds the strings to print with .format
    calling boardInfo.
    """

    if row == 1:
        print("\n\t  a   b   c")

    row = str(row)

    print("\t{} {} | {} | {}".format(row, boardInfo[row+'a'],
                                     boardInfo[row+'b'], boardInfo[row+'c']))


def get_move():
    """Gets input from player and checks if the move is legal.
    Depopulates legalMoves and/or firstMoves.
    Returns the Human Move as a string: eg. '1a'
    """

    looping = True
    time.sleep(.5)
    print("\n\tIt is your turn to move.")
    time.sleep(.5)

    while looping:
        moving = str(input("\n\tEnter your move. eg. 1a or 3c: "))
        move = moving.lower()

        if move not in legalMoves:
            time.sleep(.5)
            print('\n\n\tThat is not a legal move.\n')
        else:
            looping = False

    legalMoves.remove(move)
    if move in firstMoves:
        firstMoves.remove(move)

    return(move)


def computer_move(turn):
    """ Takes the gaming variable from main as turn.
    The first if and elif handle the first two computer moves in the game.
    calc_move handles all other moves. Returns move as a string. eg: '1a'
    """

    if turn == 1:
        move = random.choice(firstMoves)
        firstMoves.remove(move)
    elif turn == 3:
        move = random.choice(firstMoves)
        firstMoves.remove(move)
    else:
        move = calc_move()

    legalMoves.remove(move)

    return(move)


def calc_move():
    """ Calls winBlock twice. First to find the winning move as the computer, if that
    does not return a valid move, it finds a move to block a winning move.
    If there are no winning moves or moves to be blocked. The computer takes the
    remaining corner.
    """

    move = win_block('X')

    if move not in legalMoves:
        move = win_block('O')

        if move not in legalMoves:
            move = random.choice(firstMoves)

    return(move)


def win_block(piece):
    """ Takes piece passed from calcMove, a string 'X' or 'O'. move is assigned zero
    so that if a valid move is not found, win_block returns an invalid move.
    Uses a for loop to pull 3 tuples of win conditions from win[] then a for loop to
    check the state of each location. It returns the location of the empty space.
    """

    move = 0

    for three_in_a_row in win:
        empty = 0
        counter = 0
        for square in three_in_a_row:
            if boardInfo[square] == piece:
                counter+=1

            if boardInfo[square] == ' ':
                empty = square

            if counter == 2 and empty != ' ':
                move = empty

            if move in legalMoves:
                break

    return(move)


def ftw(piece):
    """ (For The Win) Takes piece from main. A string 'X' or 'O'
    Structured like win_block() with two for loops. Returns victory Bool as True if
    the game has been won.
    """

    victory = False

    for set in win:
        counter = 0
        for squares in set:
            if boardInfo[squares] == piece:
                counter += 1

            if counter == 3:
                victory = True
                break

    return(victory)


def update_board(move, piece):
    """Takes move, a string '1a' and piece from main. I mostly made this a function
    because update_board() is more readable
    """

    boardInfo[move] = piece


def initialize_game():
    """Initializes the state of the game."""
    for spots in boardInfo:
        boardInfo[spots] = ' '
    legalMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
    firstMoves =['1a','1c','3a','3c']

    return (legalMoves,firstMoves)

def play_again():
    """Asks the uses if they want to play again. This set of functions could use some
    cleaning.
    """

    print("\n\tWould you like to play again? :)")
    again = str(input("\n\ty or n: ")).lower()

    return(again)


###########################################################################
# |=========================|| MAIN ||=========================|
###########################################################################

def main():


    print('\n\tWelcome to tic-tac-toe!.')
    #mock up of pygame thing.
    interface = str(input('Would you like to play in pygame? y or n'))
    if interface == 'y':
        pytictac.main()
        break

    turn = coin_flip()

    print('\n\tHere is the game board.')
    draw_grid()

    if turn == 'first':
        human_piece = 'X'
        comp_piece = 'O'
    else:
        human_piece = 'O'
        comp_piece = 'X'












    gaming = 1
    victory = False

    while gaming<10:

        if gaming >= 2:
            time.sleep(.5)
            print("\n\tIt is the computer turn.")

        if turn != 'first':
            move = computer_move(gaming)
            update_board(move, comp_piece)
            draw_grid()
            gaming+=1

        if gaming > 4:
            if ftw(comp_piece):
                time.sleep(2.5)
                print("\n\tThe ",comp_piece,"'s have won the game!")
                break

        if gaming == 10:
            time.sleep(.5)
            print("\n\tIt's a TIE!")
            break

        move = get_move()
        update_board(move, human_piece)
        draw_grid()
        gaming += 1

        if gaming > 5:
            if ftw(human_piece):
                time.sleep(2.5)
                print("\n\tThe ",human_piece,"'s have won the game!")
                break

        if gaming == 10:
            time.sleep(1)
            print("\n\tIt's a TIE!")
            break

        turn = 'none'


main()

again = 'none'

while again != 'n':
    legalMoves,firstMoves = initialize_game()
    again = play_again()
    if again == 'y':
        main()

print("\n\tThanks a whole lot for playing!")

#Garrett Fuller
#Tic-Tac-Toe game



import time
import random
random.seed()



###########################################################################
# GLOBAL VARIABLE ASSIGNMENT
###########################################################################

#stores the state of the board for display
boardInfo = {'1a':' ', '1b':' ', '1c':' ', '2a':' ', '2b':' ', '2c':' ',
             '3a':' ', '3b':' ', '3c':' '}

#used moves are removed from this list as they are made, so I don't have to
# read the dictionary every time a move is calculated.
legalMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

#This is a list of three tuples of all the win conditions. Used to check first
# for winning moves, and second for blocking moves.
win = [('1a','1b','1c'),('2a','2b','2c'), ('3a','3b','3c'), ('1a','2a','3a'),
       ('1b','2b','3b'), ('1c','2c','3c'),('1a','2b','3c'), ('3a','2b','1c')]

#The four corners are the best opening moves for the computer. This list
# depopulates as the moves are used like leagalMoves.
firstMoves =['1a','1c','3a','3c']



###########################################################################
# : coinFlip :
###########################################################################
# Who knows?

def coin_flip():
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

###########################################################################
# : drawGrid :
###########################################################################
# Takes nothing
# Calls drawRow, drawMid
# Draws the game board


def draw_grid():

    time.sleep(.5)
    count = 0

    while count < 3:
        count+=1
        draw_row(count)

        if count <=2:
            print("\t  ==|===|==")
    time.sleep(.5)


###########################################################################
# : drawRow :
###########################################################################
# Takes an arguement called row from drawGrid (count)
# Draws the rows and grid lables. Builds the strings to print with .format
# calling boardInfo.


def draw_row(row):


    if row == 1:
        print("\n\t  a   b   c")

    row = str(row)

    print("\t{} {} | {} | {}".format(row, boardInfo[row+'a'],
                                     boardInfo[row+'b'], boardInfo[row+'c']))



###########################################################################
# : getMove :
###########################################################################
# Takes nothing.
# Returns the Human Move as a string: eg. '1a'
# Gets input from player and checks if the move is legal.
# Depopulates legalMoves and/or firstMoves.


def get_move():


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

    if move in firstMoves:
        firstMoves.remove(move)

    legalMoves.remove(move)


    return(move)



###########################################################################
# :computerMove :
###########################################################################
# Takes turn as gaming variable from main.
# The first if and elif handle the first two computer moves in the game.
# calcMove handles all other moves.


def computer_move(turn):


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



###########################################################################
# : calcMove :
###########################################################################
# Takes nothing.
# Calls winBlock twice. First to find the winning move as the computer, if that
# does not return a valid move, it finds a move to block a winning move.
# If there are no winning moves or moves to be blocked. The computer takes the
# remaining corner.

def calc_move():


    move = win_block('X')

    if move not in legalMoves:
        move = win_block('O')

        if move not in legalMoves:
            move = random.choice(firstMoves)


    return(move)



###########################################################################
# : winBlock :
###########################################################################
# Takes piece passed from calcMove, a string 'X' or 'O'.
# Uses a for loop to pull 3 tuples of win conditions from win[]
# then a for loop to check the state of each location, and place a piece
# in the empty space.


def win_block(piece):


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



###########################################################################
# : ftw : (For The Win)
###########################################################################
# Takes piece from main. A string 'X' or 'O'
# Prints to screen and Returns victory Bool as True if the game has been won.


def ftw(piece):

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


###########################################################################
# : updateBoard :
###########################################################################
# Takes move, a string '1a' and piece from main.


def update_board(move, piece):

    boardInfo[move] = piece

def initialize_game():

    for spots in boardInfo:
        boardInfo[spots] = ' '


    legalMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
    firstMoves =['1a','1c','3a','3c']
    return (legalMoves,firstMoves)

def play_again():
    print("\n\tWould you like to play again? :)")
    again = str(input("\n\ty or n: ")).lower()

    if again == 'y':
        initialize_game()

    return(again)

###########################################################################
# |=========================|| MAIN ||=========================|
###########################################################################




# Runs the program.


def main():


    print('\n\tWelcome to tic-tac-toe!.')

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


###intermitent bug where remove legal move fails
###Very interesting bug in implimentation of play again. it runs only one time.

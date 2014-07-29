#Garrett Fuller
#Tic-Tac-Toe game



import time
import random
random.seed()



###########################################################################
#   GLOBAL VARIABLE ASSIGNMENT
###########################################################################

#stores the state of the board for display
boardInfo = {'1a':' ', '1b':' ', '1c':' ', '2a':' ', '2b':' ', '2c':' ',\
             '3a':' ', '3b':' ', '3c':' '}

#used moves are removed from this list as they are made, so I don't have to
# read the dictionary every time a move is calculated.
legalMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

#This is a list of three tuples of all the win conditions. Used to check first
# for winning moves, and second for blocking moves.
win = [('1a','1b','1c'),('2a','2b','2c'), ('3a','3b','3c'), ('1a','2a','3a'),\
       ('1b','2b','3b'), ('1c','2c','3c'),('1a','2b','3c'), ('3a','2b','1c')]

#The four corners are the best opening moves for the computer. This list
# depopulates as the moves are used like leagalMoves.
firstMoves =['1a','1c','3a','3c']



###########################################################################
# : drawGrid :
###########################################################################
# Takes nothing
# Calls drawRow, drawMid
# Draws the game board


def drawGrid():


    count = 0

    while count < 3:

        count+=1
        drawRow(count)

        if count <=2:
            print("\t  ==|===|==")



###########################################################################
# : drawRow :
###########################################################################
# Takes an arguement called row from drawGrid (count)
# Draws the rows and grid lables. Builds the strings to print with .format
# calling boardInfo.

def drawRow(row):


    if row == 1:
        print("\n\t  a   b   c")

    row = str(row)

    print("\t{} {} | {} | {}".format(row, boardInfo[row+'a'],\
                                     boardInfo[row+'b'], boardInfo[row+'c']))



###########################################################################
# : getMove :
###########################################################################
# Takes nothing.
# Returns the Human Move as a string: eg. '1a'
# Gets input from player and checks if the move is legal.
# Depopulates legalMoves and/or firstMoves.

def getMove():


    looping = True

    time.sleep(1)

    print("\n\tIt is your turn to move.")

    time.sleep(1)

    while looping:

        row = str(input("\n\tEnter the row number. 1-3: "))
        column = str(input("\n\tEnter the column: a-c: "))

        move = (row+column).lower()

        if move not in legalMoves:
            time.sleep(1)
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


def computerMove(turn):


    if turn == 1:
        move = random.choice(firstMoves)
        firstMoves.remove(move)

    elif turn == 3:
        move = random.choice(firstMoves)
        firstMoves.remove(move)

    else:
        move = calcMove()

    legalMoves.remove(move)


    return(move)



###########################################################################
# : calcMove :
###########################################################################
# Takes nothing.
# Calls winBlock twice. First to find the winning move as the computer, if that
#   does not return a valid move, it finds a move to block a winning move.
# If there are no winning moves or moves to be blocked. The computer takes the
#   remaining corner.

def calcMove():


    move = winBlock('X')

    if move not in legalMoves:
        move = winBlock('O')

    if move not in legalMoves:
        move = random.choice(firstMoves)


    return(move)



###########################################################################
# : winBlock :
###########################################################################
# Takes piece passed from calcMove, a string 'X' or 'O'.
# Uses a for loop to pull 3 tuples of win conditions from win[]
#   then a for loop to check the state of each location, and place a piece
#   in the empty space.


def winBlock(piece):


    move = 0

    for three_in_a_row in win:

        empty = 0
        counter = 0

        for square in three_in_a_row:

            if boardInfo[square] == piece:
                counter+=1

            elif boardInfo[square] == ' ':
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
# Takes move, a string '1a' and turn from main.
# If the turn is not even it places an 'X', otherwise it places an 'O'
# This function should be altered to take move and piece for consistency and
#   to make the game less sensitive to who goes first. (coin flip)


def updateBoard(move, turn):

    if turn % 2 != 0:
        boardInfo[move]= 'X'

    else:
        boardInfo[move] = 'O'



###########################################################################
# |=========================||    MAIN    ||=========================|
###########################################################################
# Runs the program.


def main():


    s = time.sleep(1)

    print('\n\tWelcome to tic-tac-toe!.')

    s

    print('\n\tHere is the game board.')

    s

    drawGrid()

    s

    print("\n\tThe computer moves first.")

    s

    gaming = 1
    victory = False

    while gaming<10:

        if gaming > 2:
            s
            print("\n\tIt is the computer turn.")


        move = computerMove(gaming)
        updateBoard(move, gaming)

        s

        drawGrid()
        gaming+=1

        if gaming > 4:

            if ftw('X'):
                print("\nThe X's have won the game!")
                break

        if gaming == 10:
            print("\nIt's a TIE!")
            break


        move = getMove()
        updateBoard(move,gaming)

        s

        drawGrid()
        gaming += 1

        s

        if gaming > 5:

            if ftw('O'):
                print("\nThe O's have won the game!")
                break



main()

print("\nThanks a whole lot for playing!")

#The game works! Now I need to import sleep so everything does not happen
# instantly. Formatting for pretty Then I will look a doing a coin flip for
# who goes first. That might take some substantial thinking.

#Now I need draw row to take arguments X or O.
#I think drawRow will take count, and look up position and attribute.
#Position and attribute will be stored in a dict.

#The game board needs a function that will update it, and I need a way
# to get moves from the user. I think I will have to label the board with
# coordinates, then ask for row and column. Individual function for update
# board?

#Well, instead of preserving the board, I could just redraw the board from
# the move set each time. Not sure that will get me anything right now.

#Going to need to mock up the computer move to see how I want it to function.

#next I need to find a way to store information about the board so it can
#be drawn with X's and O's. Ideally this will

#The first thing that needs to happen after turn 3 is checking for win
#conditions. First I need to describe win conditions in a list of tipples,
#then write a function to check for them.

#I think I want to decribe a row as three positions, and check to see if two
#of three positions are filled.

#Finally! I need to check for either a win or a tie.

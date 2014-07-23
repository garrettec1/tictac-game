#Garrett Fuller
#Tic-Tac-Toe game


#The first thing I want to do, is build a display box

#Style decision
# X |   |
# ==|===|==
#   | X |
# ==|===|==
#   |   | X


#stores the state of the board in row:collum format

import time
import random
random.seed()



boardInfo = {'1a':' ', '1b':' ', '1c':' ', '2a':' ', '2b':' ', '2c':' ',\
             '3a':' ', '3b':' ', '3c':' '}

legalMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

win = [('1a','1b','1c'),('2a','2b','2c'), ('3a','3b','3c'), ('1a','2a','3a'),\
       ('1b','2b','3b'), ('1c','2c','3c'),('1a','2b','3c'), ('3a','2b','1c')]

firstMoves =['1a','1c','3a','3c']


#drawGrid will call the functions that draw individual rows
def drawGrid():


    count = 0

    while count < 3:

        count+=1
        drawRow(count)

        if count <=2:
            drawMid()



def drawRow(row):


    if row == 1:
        print("\n\t  a   b   c")

    row = str(row)

    print("\t{} {} | {} | {}".format(row, boardInfo[row+'a'],\
                                     boardInfo[row+'b'], boardInfo[row+'c']))


def drawMid():


    print("\t  ==|===|==")



def getMove():


    looping = True

    time.sleep(1.5)

    print("\n\tIt is your turn to move.")

    time.sleep(1)

    while looping:

        row = str(input("\n\tEnter the row number. 1-3: "))
        column = str(input("\n\tEnter the column: a-c: "))

        move = (row+column).lower()

        if move not in legalMoves:
            time.sleep(.9)
            print('\n\n\tThat is not a legal move.\n')

        else:
            looping = False

    if move in firstMoves:
        firstMoves.remove(move)

    legalMoves.remove(move)


    return(move)



def computerMove(boardInfo, legalMoves, turn):




    if turn == 1:
        move = random.choice(firstMoves)
        firstMoves.remove(move)

    elif turn == 3:
        move = random.choice(firstMoves)
        firstMoves.remove(move)

    else:
        move = calcMove(boardInfo)

    if move not in legalMoves:
        move = random.choice(firstMoves)

    legalMoves.remove(move)


    return(move)

#what is the best way to deal with the computers second move? currently the
# game will crash if the human chooses to move the opposite corner from the
# computer. .remove will only work if it is in the list. Oh conditional!

def calcMove(boardInfo):


    move = winBlock('X')

    if move not in legalMoves:
        move = winBlock('O')


    return(move)

#okay... so calcMove fails if there is no blockable move or winning move.

def winBlock(piece):


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



def updateBoard(move, turn):

    if turn % 2 != 0:
        boardInfo[move]= 'X'

    else:
        boardInfo[move] = 'O'



def main():


    print('\n\tWelcome to tic-tac-toe!.')

    time.sleep(1.5)

    print('\n\tHere is the game board.')

    time.sleep(1)

    drawGrid()

    time.sleep(2)

    print("\n\tThe computer moves first.")

    time.sleep(1)

    gaming = 1
    victory = False

    while gaming<10:

        if gaming > 2:
            time.sleep(1)
            print("\n\tIt is the computer turn.")

        move = computerMove(boardInfo, legalMoves, gaming)
        updateBoard(move, gaming)

        time.sleep(1.8)

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

        time.sleep(2)

        drawGrid()
        gaming += 1

        time.sleep(2)

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

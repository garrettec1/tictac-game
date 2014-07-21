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
boardInfo = {'1a':' ', '1b':' ', '1c':' ', '2a':' ', '2b':' ', '2c':' ',\
             '3a':' ', '3b':' ', '3c':' '}

legalMoves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

#drawGrid will call the functions that draw individual rows
def drawGrid():

    count = 0

    while count < 3:
        count+=1
        drawRow(count)
        if count <=2:
            drawMid()


#Needs to be refactored to build the string with game pieces.
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

    while looping:
        print("It is your turn to move.")
        row = str(input("Enter the row number. 1-3: "))
        column = str(input("Enter the column: a-c: "))
        move = (row+column).lower()

        if move not in legalMoves:
            print('That is not a legal move')
        else:
            looping = False
    legalMoves.remove(move)

    return(move)


def computerMove(boardInfo, legalMoves, turn):
    if turn == 1:
        move = '1a'
    elif turn == 3:
        move = '3c'
    else:
        move = calcMove(boardInfo)

    legalMoves.remove(move)
    return(move)

win = [('1a','1b','1c'),('2a','2b','2c'), ('3a','3b','3c'), ('1a','2a','3a'),\
       ('1b','2b','3b'), ('1c','2c','3c'),('1a','2b','3c'), ('3a','2b','1c')]

def calcMove(boardInfo):


    move = winBlock('X')
    if move not in legalMoves:
        move = winBlock('O')

    return(move)



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


#The first thing that needs to happen after turn 3 is checking for win
#conditions. First I need to describe win conditions in a list of tipples,
#then write a function to check for them.

#I think I want to decribe a row as three positions, and check to see if two
#of three positions are filled.

def updateBoard(move, turn):

    print(turn)
    if turn % 2 != 0:
        boardInfo[move]= 'X'
    else:
        boardInfo[move] = 'O'

def main():
    drawGrid()
    gaming = 1
    while gaming<8:

        move = computerMove(boardInfo, legalMoves, gaming)
        updateBoard(move, gaming)
        drawGrid()
        gaming+=1
        move = getMove()
        updateBoard(move,gaming)
        drawGrid()
        gaming += 1


main()
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

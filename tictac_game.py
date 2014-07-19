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
    if turn == 0:
        move = '1a'
    elif turn == 2:
        move = '3c'
    else:
        move = calcMove(boardInfo, legalMoves, turn)
    return(move)

def calcMove(boardInfo, legalMoves, turn):

    return('2b')

def updateBoard(move, turn):

    print(turn)
    if turn % 2 != 0:
        boardInfo[move]= 'X'
    else:
        boardInfo[move] = 'O'


drawGrid()
gaming = 0
while gaming<3:

    move = computerMove(boardInfo, legalMoves, gaming)
    gaming += 1
    updateBoard(move, gaming)
    drawGrid()
    gaming+=1
    move = getMove()
    updateBoard(move,gaming)
    drawGrid()
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

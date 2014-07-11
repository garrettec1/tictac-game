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
    print("It is your turn to move.")
    row = str(input("Enter the row number. 1-3: "))
    column = str(input("Enter the column: a-c: "))
    move = (row+column).lower()
    print(move)

    return(move)


def updateBoard(move):
    boardInfo[move] = 'X'


#Now I need draw row to take arguments X or O.
#I think drawRow will take count, and look up position and attribute.
#Position and attribute will be stored in a dict.

#The game board needs a function that will update it, and I need a way
# to get moves from the user. I think I will have to label the board with
# coordinates, then ask for row and column. Individual function for update
# board?




#next I need to find a way to store information about the board so it can
#be drawn with X's and O's. Ideally this will

drawGrid()

move = getMove()
updateBoard(move)
drawGrid()

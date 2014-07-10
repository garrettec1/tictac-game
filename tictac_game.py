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
    print()
    count = 0
    while count < 3:
        count+=1
        drawRow(count)
        if count <=2:
            drawMid()


#Needs to be refactored to build the string with game pieces.
def drawRow(row):
    row = str(row)
    print("\t{} | {} | {}".format(boardInfo[row+'a'], boardInfo[row+'b'],\
                                  boardInfo[row+'c']))

def drawMid():
    print("\t==|===|==")





#Now I need draw row to take arguments X or O.
#I think drawRow will take count, and look up position and attribute.
#Position and attribute will be stored in a dict.



#next I need to find a way to store information about the board so it can
#be drawn with X's and O's. Ideally this will

drawGrid()

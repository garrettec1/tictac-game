#Garrett Fuller
#Tic-Tac-Toe game


#The first thing I want to do, is build a display box

#Style decision
# X |   |
# ==|===|==
#   | X |
# ==|===|==
#   |   | X

#drawGrid will call the functions that draw individual rows
def drawGrid():
    print()
    count = 0
    while count < 3:
        count+=1
        drawRow(count)
        if count <=2:
            drawMid()

def drawRow(rowNumber):
    print("\t  |   |  ")

def drawMid():
    print("\t==|===|==")





#Now I need draw row to take arguments X or O.
#I think drawRow will take count, and look up position and attribute.
#Position and attribute will be stored in a dict.

#next I need to find a way to store information about the board so it can
#be drawn with X's and O's. Ideally this will

drawGrid()

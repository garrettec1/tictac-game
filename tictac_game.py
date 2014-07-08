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
    drawRow()
    drawMid()
    drawRow()
    drawMid()
    drawRow()

def drawRow():
    print("\t  |   |  ")

def drawMid():
    print("\t==|===|==")


drawGrid()

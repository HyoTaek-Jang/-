
X = "X"
B = "B"
W = "W"

board = [
    [W, B, B, X, W, W, X, X, X, X, X, X, X],
    [B, X, B, X, W, X, W, X, X, W, X, X, W],
    [W, B, X, X, X, W, X, W, X, W, X, X, X],
    [B, X, B, X, X, X, X, X, X, X, X, X, W],
    [X, B, B, X, X, W, X, B, X, B, X, X, X],
    [B, X, X, X, X, W, X, X, X, X, B, X, X],
    [X, X, B, X, X, X, W, X, X, X, X, X, B],
    [X, X, X, X, X, B, X, X, B, X, X, X, X],
    [X, X, B, X, X, X, B, X, X, W, X, X, X],
    [X, X, X, X, X, X, X, B, X, X, X, X, X],
    [W, B, X, X, X, X, X, X, B, W, W, X, W],
    [B, X, B, X, X, X, X, W, W, W, X, X, X],
    [X, X, X, X, X, X, X, X, X, X, X, X, X],
]

totalCountB = 0;
totalCountW = 0;
countB = 0;
countW = 0;
curPosition = [0,0]
curColor = ""
curdirection = ""

def checkNear(curPosition, curColor):


for i in range(13):
    for j in range(13):
        if(board[i][j]== "B"):
            countB+=1
        elif(board[i][j] == "W"):
            countW+=1


print('white :',countW,', black :' ,countB)
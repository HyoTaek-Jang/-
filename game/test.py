from OMOK import getWinner


X = None
B = "B"
W = "W"

board = [
    [B, B, W, B, B, W, X, X, X, X, X, X, X],
    [B, X, B, X, W, W, W, X, X, W, X, X, W],
    [W, B, X, X, X, W, X, W, X, W, X, X, X],
    [B, X, B, X, X, X, X, X, W, X, X, X, W],
    [X, B, B, X, X, W, X, B, B, W, X, X, X],
    [B, X, X, X, X, W, X, X, B, B, W, X, X],
    [X, X, B, X, W, X, W, X, X, B, B, X, B],
    [X, X, X, X, X, B, X, X, B, X, X, X, X],
    [X, X, B, X, X, X, B, X, X, W, X, X, X],
    [X, X, X, X, X, X, X, B, X, X, X, W, X],
    [W, B, X, X, X, X, X, X, B, W, W, X, W],
    [B, X, B, X, X, W, W, X, W, W, X, X, X],
    [X, X, X, X, X, X, X, X, X, X, X, X, X],
]

print(getWinner(board))
#
# X = "X"
# B = "B"
# W = "W"
#
# board = [
#     [B, B, B, B, B, W, X, X, X, X, X, X, X],
#     [B, X, B, X, W, X, W, X, X, W, X, X, W],
#     [W, B, X, X, X, W, X, W, X, W, X, X, X],
#     [B, X, B, X, X, X, X, X, X, X, X, X, W],
#     [X, B, B, X, X, W, X, B, X, B, X, X, X],
#     [B, X, X, X, X, W, X, X, X, X, B, X, X],
#     [X, X, B, X, X, X, W, X, X, X, X, X, B],
#     [X, X, X, X, X, B, X, X, B, X, X, X, X],
#     [X, X, B, X, X, X, B, X, X, W, X, X, X],
#     [X, X, X, X, X, X, X, B, X, X, X, X, X],
#     [W, B, X, X, X, X, X, X, B, W, W, X, W],
#     [B, X, B, X, X, W, W, W, W, W, X, X, X],
#     [X, X, X, X, X, X, X, X, X, X, X, X, X],
# ]
#
#
#
# def getWinner(board):
#     global totalCountB
#     global totalCountW
#     global count
#     global curPosition
#     global curColor
#     global curDirection
#     global winB
#     global winW
#     totalCountB = 0
#     totalCountW = 0
#     winB = 0
#     winW = 0
#
#     for i in range(13):
#         for j in range(13):
#             curPosition = [i,j]
#             curDirection = 0
#             # if(예외조건들...)
#             #     return "X"
#             if(board[i][j]== "B"):
#                 curColor = "B"
#                 totalCountB += 1
#                 if(checkNear(board, curPosition, curColor, curDirection, 0) == 'Win'):
#                     winB = 'Win'
#             elif(board[i][j] == "W"):
#                 curColor = "W"
#                 totalCountW += 1
#                 if (checkNear(board, curPosition, curColor, curDirection, 0) == 'Win'):
#                     winW = 'Win'
#
#     if(winB=="Win" and winW=="Win"):
#         return 'X'
#     elif(winB=="Win"):
#         return 'B'
#     elif(winW=="Win"):
#         return 'W'
#     else:
#         return None
#
# def checkNear(_board, _curPosition, _curColor, _curDirection, count):
#     global winB
#     global winW
#     if(_curDirection == 0):
#         if(_curPosition[1]+1<13):
#             if(board[_curPosition[0]][_curPosition[1]+1] == _curColor):
#                 count=2
#                 curPosition = [_curPosition[0],_curPosition[1]+1]
#                 curDirection = "Right"
#                 checkNear(_board, curPosition, _curColor, curDirection,count)
#         if (_curPosition[0] + 1 < 13 and _curPosition[1] + 1 < 13):
#             if(board[_curPosition[0]+1][_curPosition[1]+1] == _curColor):
#                 count=2
#                 curPosition = [_curPosition[0]+1,_curPosition[1]+1]
#                 curDirection = "RightBottom"
#                 checkNear(_board, curPosition, _curColor, curDirection,count)
#         if (_curPosition[0] + 1 < 13):
#             if(board[_curPosition[0]+1][_curPosition[1]] == _curColor):
#                 count=2
#                 curPosition = [_curPosition[0]+1,_curPosition[1]]
#                 curDirection = "Bottom"
#                 checkNear(_board, curPosition, _curColor, curDirection,count)
#         if (_curPosition[0] + 1 < 13 and _curPosition[1]-1>=0):
#             if(board[_curPosition[0]+1][_curPosition[1]-1] == _curColor):
#                 count=2
#                 curPosition = [_curPosition[0]+1,_curPosition[1]-1]
#                 curDirection = "LeftBottom"
#                 checkNear(_board, curPosition, _curColor, curDirection,count)
#
#
#
#     if(_curDirection == "Right"):
#         if (board[_curPosition[0]][_curPosition[1] + 1] == _curColor):
#             curPosition = [_curPosition[0],_curPosition[1] + 1]
#             count += 1
#             checkNear(_board, curPosition, _curColor, _curDirection,count)
#     if(_curDirection == "RightBottom"):
#         if (board[_curPosition[0]+1][_curPosition[1] + 1] == _curColor):
#             curPosition = [_curPosition[0]+1,_curPosition[1] + 1]
#             count += 1
#             checkNear(_board, curPosition, _curColor, _curDirection,count)
#     if(_curDirection == "Bottom"):
#         if (board[_curPosition[0]+1][_curPosition[1]] == _curColor):
#             curPosition = [_curPosition[0]+1,_curPosition[1]]
#             count += 1
#             checkNear(_board, curPosition, _curColor, _curDirection,count)
#     if(_curDirection == "LeftBottom"):
#         if (board[_curPosition[0]+1][_curPosition[1] -1] == _curColor):
#             curPosition = [_curPosition[0]+1,_curPosition[1] -1]
#             count += 1
#             checkNear(_board, curPosition, _curColor, _curDirection,count)
#     if count == 5:
#        winB = "Win"
#
# getWinner(board)
# print('winb', winB, ' winw',winW)1
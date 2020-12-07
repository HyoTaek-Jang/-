# omok_201721070

def getWinner(board):
    totalCountB = 0
    totalCountW = 0
    winB = False
    winW = False

    for i in range(13):
        for j in range(13):
            curPosition = [i, j]
            if board[i][j] == "B":
                curColor = "B"
                totalCountB += 1
                # 돌 주변으로 이어져있나 체크
                if checkNear(board, curColor, curPosition):
                    winB = True
            elif board[i][j] == "W":
                curColor = "W"
                totalCountW += 1
                # 돌 주변으로 이어져있나 체크
                if checkNear(board, curColor, curPosition):
                    winW = True

    # 예외조건 확인 및 승자 체크
    if (winB and winW) or totalCountW > totalCountB or totalCountW + 2 <= totalCountB:
        return 'X'
    elif winB:
        return 'B'
    elif winW:
        return 'W'
    else:
        return None


def checkNear(board, curColor, curPosition):
    checkWin = False

    # 오른쪽으로 오목이 완성됐나 체크
    temp = curPosition[:]
    count = 1
    while temp[1] + 1 < 13:
        temp[1] += 1
        if board[temp[0]][temp[1]] == curColor:
            count += 1
        else:
            break
    if count == 5:
        checkWin = True

    # 우측하단으로 오목이 완성됐나 체크
    temp = curPosition[:]
    count = 1
    while temp[0] + 1 < 13 and temp[1] + 1 < 13:
        temp[1] += 1
        temp[0] += 1
        if board[temp[0]][temp[1]] == curColor:
            count += 1
        else:
            break
    if count == 5:
        checkWin = True

    # 아래쪽으로 오목이 완성됐나 체크
    temp = curPosition[:]
    count = 1
    while temp[0] + 1 < 13:
        temp[0] += 1
        if board[temp[0]][temp[1]] == curColor:
            count += 1
        else:
            break
    if count == 5:
        checkWin = True

    # 좌측하단으로 오목이 완성됐나 체크
    temp = curPosition[:]
    count = 1
    while temp[0] + 1 < 13 and temp[1] - 1 >= 0:
        temp[0] += 1
        temp[1] -= 1
        if board[temp[0]][temp[1]] == curColor:
            count += 1
        else:
            break
    if count == 5:
        checkWin = True

    # checkWin 반환
    return checkWin

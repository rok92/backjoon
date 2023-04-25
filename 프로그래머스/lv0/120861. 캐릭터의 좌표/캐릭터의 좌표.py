def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    xlimit = board[0] // 2
    ylimit = board[1] // 2
    for i in keyinput:
        if i == 'right':
            if x >= xlimit:
                x = xlimit
            else:
                x += 1
        elif i == 'left':
            if x <= -xlimit:
                x = -xlimit
            else:
                x -= 1
        elif i == 'up':
            if y >= ylimit:
                y = ylimit
            else:
                y += 1
        elif i == 'down':
            if y <= -ylimit:
                y = -ylimit
            else:
                y -= 1
    answer.append(x)
    answer.append(y)
    return answer
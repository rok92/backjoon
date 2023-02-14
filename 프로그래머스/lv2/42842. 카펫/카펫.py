def solution(brown, yellow):
    answer = []
    y_row = 0
    y_col = 0
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_row = yellow // i
            y_col = i
            if (y_row*2 + y_col*2) + 4 == brown:
                answer.append(y_row+2)
                answer.append(y_col+2)
                return answer

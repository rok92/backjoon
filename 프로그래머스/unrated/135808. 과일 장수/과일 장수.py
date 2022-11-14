def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    for i in range(0, len(score), m) :
        temp = score[i:i+m]
        if len(temp) == m :
            answer += min(temp) * m
    return answer
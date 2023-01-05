def solution(money):
    answer = []
    cnt = money // 5500
    rest = money % 5500
    answer.append(cnt)
    answer.append(rest)
    return answer
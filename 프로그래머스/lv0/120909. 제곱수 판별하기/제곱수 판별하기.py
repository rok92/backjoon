def solution(n):
    answer = 0
    temp = n ** 0.5
    if int(temp) == temp :
        answer = 1
    else :
        answer = 2
    return answer
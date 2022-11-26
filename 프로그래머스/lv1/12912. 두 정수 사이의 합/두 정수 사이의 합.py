def solution(a, b):
    answer = 0
    if a < b :
        answer = list(range(a, b+1))
    else :
        answer = list(range(b, a+1))
    
    return sum(answer)
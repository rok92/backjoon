def solution(n):
    answer = 0
    k = n**0.5
    if k.is_integer():
        answer = (k+1)**2
    else :
        answer = -1
    return answer
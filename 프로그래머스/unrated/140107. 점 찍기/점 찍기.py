import math

def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        a = math.sqrt(d*d - i*i) 
        answer += (a // k+1)
    print(answer)
    return answer
def solution(a, b):
    answer = 0
    for i in range(len(b)):
        answer += (a[i]*b[i])
    return answer
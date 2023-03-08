def solution(n):
    answer = 0
    n = list(str(n))
    a = list(map(int, n))
    for i in range(len(a)):
        answer += a[i]
    return answer
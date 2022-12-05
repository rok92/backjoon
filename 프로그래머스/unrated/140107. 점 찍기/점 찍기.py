def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        a = (d*d - i*i) ** (0.5)
        answer += (a // k+1)
    print(answer)
    return answer
def solution(n):
    answer = []
    answer.append(0)
    answer.append(1)
    for i in range(2, n + 1):
        k = answer[i-1] + answer[i-2]
        answer.append(k%1234567)
    return answer[-1]
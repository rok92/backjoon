def solution(n):
    k = list(str(n))
    answer = list(map(int, k[::-1]))
    print(answer)
    return answer
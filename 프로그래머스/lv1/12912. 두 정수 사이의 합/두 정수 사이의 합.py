def solution(a, b):
    answer = []
    if a == b:
        return a
    elif a > b:
        for i in range(b, a+1):
            answer.append(i)
    elif a < b:
        for i in range(a, b+1):
            answer.append(i)
    return sum(answer)
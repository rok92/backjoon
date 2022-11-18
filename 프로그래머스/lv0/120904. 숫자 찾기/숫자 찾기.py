def solution(num, k):
    answer = 0
    a = str(num)
    b = str(k)
    for i in a :
        answer += 1
        if i == b :
            return answer
    if b not in a :
        return -1
    return answer
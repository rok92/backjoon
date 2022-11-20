def solution(before, after):
    answer = 0
    a = list(before)
    b = list(after)
    a.sort()
    b.sort()
    if a == b :
        answer = 1
    return answer
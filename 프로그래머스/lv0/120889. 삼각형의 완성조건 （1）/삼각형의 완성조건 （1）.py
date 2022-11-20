def solution(sides):
    answer = 0
    a = max(sides)
    sides.remove(a)
    print(sides)
    if sum(sides) <= a :
        answer = 2
    else :
        answer = 1
    return answer
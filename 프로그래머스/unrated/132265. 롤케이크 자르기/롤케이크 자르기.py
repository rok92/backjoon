from collections import Counter

def solution(topping):
    answer = 0
    cake_top = Counter(topping)
    check = set()
    for i in topping:
        cake_top[i] -= 1
        check.add(i)
        if cake_top[i] == 0:
            cake_top.pop(i)
        if len(cake_top) == len(check):
            answer += 1
        
    return answer
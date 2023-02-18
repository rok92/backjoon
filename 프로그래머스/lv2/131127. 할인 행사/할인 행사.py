from collections import Counter

def solution(want, number, discount):
    answer = 0
    diction = {}
    for i in range(len(want)):
        diction[want[i]] = number[i]
    for i in range(len(discount)):
        if diction == Counter(discount[i:i+10]):
            print(diction)
            answer += 1
    return answer
from collections import Counter

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            print(i, a)
            array.remove(a)
        if i == 0: return a
    return -1

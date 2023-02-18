from itertools import chain

def solution(food):
    answer = []
    for i in range(1, len(food)) :
        for _ in range(food[i]//2):
            answer.append(i)
    answer = ''.join(map(str, answer + [0] + answer[::-1]))
    return answer

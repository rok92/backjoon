from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons, len(dungeons)):
        count = 0
        tmp = k
        for a, b in i:
            if tmp >= a :
                tmp -= b
                count += 1
        answer = max(answer, count)
    return answer
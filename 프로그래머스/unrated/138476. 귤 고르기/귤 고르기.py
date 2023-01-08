from collections import Counter

def solution(k, tangerine):
    answer = 0
    s = 0
    tangerine.sort(reverse = True)
    tan = Counter(tangerine).most_common()
    for i in tan:
        s += i[1]
        answer += 1
        if s >= k:
            return answer
    return answer
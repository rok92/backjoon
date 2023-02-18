from collections import Counter



def solution(k, tangerine):
    answer = 0
    tan = Counter(tangerine)
    tanger = sorted(tan.values(), reverse = True)
    for i in tanger:
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer
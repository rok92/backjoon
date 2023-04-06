from collections import Counter

def solution(array):
    answer = []
    a = Counter(array)
    mc = a.most_common()
    maxi = mc[0][1]
    
    for i in mc:
        if i[1] == maxi:
            answer.append(i[0])
    if len(answer) >= 2:
        return -1
    else:
        return answer[0]

def solution(clothes):
    answer = 1
    closet = {}
    for i in clothes:
        key = i[1]
        value = i[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]
    for i in closet.keys():
        answer *= len(closet[i])+1
        
    return answer-1
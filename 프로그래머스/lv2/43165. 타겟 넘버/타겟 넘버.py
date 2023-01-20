def solution(numbers, target):
    answer = 0
    k = [0]
    for i in numbers:
        tmp = []
        for j in k:
            tmp.append(j+i)
            tmp.append(j-i)
        k = tmp
    for i in k:
        if i == target:
            answer += 1
    return answer
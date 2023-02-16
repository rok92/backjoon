def solution(left, right):
    answer = []
    for i in range(left, right+1):
        count_i = 0
        for j in range(1, i+1):
            if i % j == 0:
                count_i += 1
        if count_i % 2 == 0:
            answer.append(i)
        else:
            answer.append(-i)
    print(answer)
    return sum(answer)


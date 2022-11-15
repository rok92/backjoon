def solution(array):
    answer = 0
    stack = []
    for i in array :
        for j in range(len(str(i))) :
            if str(i)[j] == '7' :
                answer += 1
    return answer
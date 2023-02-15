def solution(x):
    answer = True
    array = list(str(x))
    sum_arr = 0
    for i in range(len(array)):
        sum_arr += int(array[i])
        if x % sum_arr == 0:
            answer = True
        else:
            answer = False
    return answer
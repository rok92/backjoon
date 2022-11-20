def solution(array, n):
    answer = 0
    array.sort()
    a = n + 100
    for i in array :
        if abs(i - n) < a :
            a = abs(i-n)
            answer = i
    return answer
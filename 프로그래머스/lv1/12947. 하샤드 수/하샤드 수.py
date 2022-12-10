def solution(x):
    answer = True
    arr = list(str(x))
    a = 0
    for i in range(len(arr)):
        a += int(arr[i])
        if x % a == 0:
            answer = True
        else:
            answer = False
        
    return answer
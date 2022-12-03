def solution(arr):
    answer = []
    arr.remove(min(arr))
    answer = arr
    if len(arr) < 2:
        answer.append(-1)
        
    return answer
def solution(arr):
    answer = arr
    answer.remove(min(answer))
    if len(answer) < 2:
        answer = [-1]
    return answer
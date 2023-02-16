def solution(arr):
    answer = []
    answer = arr
    answer.remove(min(answer))
    if len(answer) < 2:
        answer.append(-1)
    return answer
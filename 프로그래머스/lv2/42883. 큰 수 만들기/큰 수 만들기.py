def solution(number, k):
    answer = [number[0]]
    for num in number[1:]:
        while len(answer) > 0 and k > 0 and answer[-1] < num:
            k -= 1
            answer.pop()
        answer.append(num)
    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)
    
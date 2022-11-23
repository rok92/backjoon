def solution(number, k):
    answer = []
    for i in number :
        while answer and k > 0 and answer[-1] < i :
            answer.pop()
            k -= 1
        answer.append(i)
    answer = ''.join(answer[:len(number)-k])
    return answer
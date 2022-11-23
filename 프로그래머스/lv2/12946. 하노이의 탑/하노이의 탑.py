def solution(n):
    answer = []
    def top(n, start, end, mid) :
        if n == 1 :
            answer.append([start, end])
        else :
            top(n-1, start, mid, end)
            answer.append([start, end])
            top(n-1, mid, end, start)
    top(n, 1, 3, 2)
    return answer
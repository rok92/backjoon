def solution(s, n):
    answer = ''
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        if i in lower:
            a = lower.find(i)+n
            answer += lower[a%26]
        elif i in upper:
            a = upper.find(i)+n
            answer += upper[a%26]
        else:
            answer += ' '
    return answer
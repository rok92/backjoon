def solution(s):
    answer = ""
    for i in s:
        if s.count(i) == 1:
            answer += i
    answer  = ''.join(sorted(answer))
    return answer
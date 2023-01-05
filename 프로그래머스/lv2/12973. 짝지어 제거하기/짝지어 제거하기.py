def solution(s):
    answer = []
    for i in range(len(s)):
        if not answer:
            answer.append(s[i])
        else:
            if s[i] == answer[-1]:
                answer.pop()
            else:
                answer.append(s[i])
    if answer: return 0
    else: return 1

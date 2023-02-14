def solution(s):
    answer = []
    for i in range(len(s)):
        if not answer:
            answer.append(s[i])
        else:
            if answer[-1] == s[i]:
                answer.pop()
            else:
                answer.append(s[i])
    if len(answer) == 0:
        return 1
    else:
        return 0

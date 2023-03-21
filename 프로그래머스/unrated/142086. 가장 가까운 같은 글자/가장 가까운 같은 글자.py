def solution(s):
    answer = []
    lang = {}
    for i in range(len(s)):
        if s[i] not in lang:
            answer.append(-1)
        else:
            answer.append(i-lang[s[i]])
        lang[s[i]] = i
    return answer
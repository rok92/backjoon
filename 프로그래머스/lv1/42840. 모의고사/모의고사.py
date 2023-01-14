def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    b1, b2, b3 = 0, 0, 0
    for i in range(len(answers)):
        q1 = i % 5
        q2 = i % 8
        q3 = i % 10
        if a1[q1] == answers[i]:
            b1 += 1
        if a2[q2] == answers[i]:
            b2 += 1
        if a3[q3] == answers[i]:
            b3 += 1
    s = max(b1, b2, b3)
    if s == b1:
        answer.append(1)
    if s == b2:
        answer.append(2)
    if s == b3:
        answer.append(3)
    return answer
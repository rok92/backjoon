def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s:
        print(i)
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    print(answer)
    return answer[0:-1]
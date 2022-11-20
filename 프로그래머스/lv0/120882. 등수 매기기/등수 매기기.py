def solution(score):
    answer = []
    a = []
    for i in score :
        a.append(sum(i) / len(i))
    b = sorted(a, reverse = True)
    print(a)
    for i in a :
        answer.append(b.index(i)+1)
    return answer
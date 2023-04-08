
def solution(emergency):
    answer = []
    sort_e = sorted(emergency, reverse = True)
    print(sort_e)
    for i in emergency:
        answer.append(sort_e.index(i)+1)
    return answer
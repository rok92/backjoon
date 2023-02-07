def solution(s):
    answer = True
    p = s.count('P') + s.count('p')
    y = s.count('Y') + s.count('y')
    
    if p != y:
        answer = False
    else: answer = True
    return answer
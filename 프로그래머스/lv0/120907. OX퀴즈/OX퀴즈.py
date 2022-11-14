def solution(quiz):
    answer = []
    for i in range(len(quiz)) :
        if eval(quiz[i].replace('=', '==')) :
            answer.append("O")
        else :
            answer.append("X")
            
    return answer
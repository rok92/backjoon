def solution(hp):
    answer = 0
    while hp >= 0 :
        if hp % 5 == 0:
            answer += (hp//5)
            break
        if hp < 3 :
            hp -= 1
            answer += 1
        else :
            hp -= 3
            answer += 1
    return answer
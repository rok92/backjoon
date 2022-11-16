def solution(order):
    answer = 0
    array = ['3', '6', '9']
    order = str(order)
    for i in order :
        if i in array :
            answer += 1
    return answer
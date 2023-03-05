def solution(my_string):
    answer = []
    arString = list(my_string)
    for i in range(len(arString)):
        if arString[i].isdigit():
            answer.append(arString[i])
    answer.sort()
    answer = list(map(int, answer))
    return answer
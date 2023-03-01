def solution(my_string):
    answer = []
    my_string = list(my_string)
    mom =['a', 'i', 'u', 'e', 'o']
    for i in range(len(my_string)):
        if my_string[i] not in mom:
            answer.append(my_string[i])
        
    return ''.join(answer)
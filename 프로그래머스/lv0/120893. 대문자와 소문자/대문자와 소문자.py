def solution(my_string):
    answer = ''
    a = list(my_string)
    for i in a :
        if i.isupper() :
            answer += i.lower()
        else :
            answer += i.upper()
    return answer
def solution(rsp):
    answer = ''
    rsp = list(rsp)
    for i in rsp:
        if i == '2':
            answer += '0'
        if i == '0':
            answer += '5'
        if i == '5':
            answer += '2'
    return answer
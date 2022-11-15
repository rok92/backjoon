def solution(str1, str2):
    answer = 0
    stack = []
    for i in range(len(str1)) :
        stack.append(str1[i])
    stack = ''.join(stack)
    if str2 in stack :
        answer = 1
    else :
        answer = 2
    return answer
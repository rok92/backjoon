def solution(str1, str2):
    stack = []
    for i in str1:
        stack.append(i)
    stack = ''.join(stack)
    print(stack)
    if str2 in stack:
        return 1
    else:
        return 2

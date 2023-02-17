def solution(s):
    list_s = []
    for i in s:
        if i == '(':
            list_s.append(i)
        if i == ')':
            try:
                list_s.pop()
            except IndexError:
                    return False
            
    return len(list_s) == 0
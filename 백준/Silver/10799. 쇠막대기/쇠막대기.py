def cut_iron_sticks(sticks):
    sticks = sticks.replace('()', 'l') # 레이저를 구분하기 위해 괄호를 l로 바꿈
    stack = []
    count = 0
    for s in sticks:
        if s == '(':
            stack.append(s)
        elif s == 'l':
            count += len(stack)
        else: # s == ')'
            stack.pop()
            count += 1
    return count

n = input()

print(cut_iron_sticks(n))
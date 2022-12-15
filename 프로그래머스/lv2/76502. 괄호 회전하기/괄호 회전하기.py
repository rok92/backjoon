def bracket(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    return 1 if len(stack) == 0 else 0

def solution(s):
    answer = 0
    for i in range(len(s)):
        if bracket(s):
            answer += 1
        s = s[1:] + s[:1]
    return answer


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
def solution(s):
    count = 0
    for i in range(len(s)):
        stack = []
        for j in s:
            if not stack:
                stack.append(j)
                continue
            if stack[-1] == '[' and j == ']':
                stack.pop()
            elif stack[-1] == '{' and j == '}':
                stack.pop()
            elif stack[-1] == '(' and j == ')':
                stack.pop()
            else:
                stack.append(j)
        s = s[1:] + s[0]
        if not stack:
            count += 1
    return count
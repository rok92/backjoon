import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  bracket = input()

  stack = []
  for i in bracket:
    if i == '(':
      stack.append(i)
    elif i == ')':
      if len(stack) == 0:
        print('NO')
        break
      else:
        stack.pop()

  else:
    if len(stack) == 0:
      print('YES')
    else:
      print('NO')
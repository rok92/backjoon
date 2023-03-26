import sys
input = sys.stdin.readline

n = int(input())

count = 1
stack = []
pp = []
result = True

for _ in range(n):
  num = int(input())

  while count <= num:
    stack.append(count)
    count += 1
    pp.append('+')
  if stack[-1] == num:
    stack.pop()
    pp.append('-')
  else:
    result = False
    break

if result == False:
  print('NO')
else:
  for i in pp:
    print(i)
import sys
input = sys.stdin.readline

n = int(input())
nge = list(map(int, input().split()))
stack = []

answer = [-1] * n

for i in range(n):
  while len(stack) != 0 and nge[stack[-1]] < nge[i]:
    answer[stack.pop()] = nge[i]
  stack.append(i)
    
print(*answer)
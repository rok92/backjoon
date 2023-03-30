import sys
input = sys.stdin.readline

A = int(input())
nums = list(map(int, input().split()))
stack = []
nge = [-1] * A

for i in range(A):
  while stack and nums[stack[-1]] < nums[i]:
    nge[stack.pop()] = nums[i]
  stack.append(i)
answer = ' '.join(map(str, nge))
print(answer)
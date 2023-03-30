import sys
from collections import Counter
input = sys.stdin.readline

A = int(input())
nums = list(map(int, input().split()))
stack = []
count = Counter(nums)
ngf = [-1] * A

for i in range(A):
  while stack and count[nums[stack[-1]]] <count[nums[i]]:
    ngf[stack.pop()] = nums[i]
  stack.append(i)

print(' '.join(map(str, ngf)))

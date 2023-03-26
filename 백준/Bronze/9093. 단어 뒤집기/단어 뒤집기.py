import sys

T = int(sys.stdin.readline())

for _ in range(T):
  sentence = sys.stdin.readline().split()
  stack = []

  for i in range(len(sentence)):
    stack.append(sentence[i][::-1])

  print(' '.join(stack))
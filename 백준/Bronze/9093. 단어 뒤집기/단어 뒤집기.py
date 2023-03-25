import sys

T = int(sys.stdin.readline())

for _ in range(T):
  sentence = sys.stdin.readline().split()
  l_sentence = list(sentence)
  stack = []

  for i in range(len(l_sentence)):
    stack.append(l_sentence[i][::-1])

  print(' '.join(stack))
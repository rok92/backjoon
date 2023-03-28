import sys
input = sys.stdin.readline

s = list(input().rstrip())

idx = 0
left = 0
while idx < len(s):
  if s[idx] == '<':
    idx += 1
    while s[idx] != '>':
      idx += 1
    idx += 1
  elif s[idx].isalnum():
    left = idx
    while idx<len(s) and s[idx].isalnum():
      idx += 1
    re = s[left:idx]
    re.reverse()
    s[left:idx] = re
  else:
    idx += 1

print((''.join(s)))
import sys
input = sys.stdin.readline

s = list(input().strip())
start = 0
idx = 0
while idx < len(s):
    if s[idx] == '<':
      idx += 1
      while s[idx] != '>':
        idx += 1
      idx += 1
    elif s[idx].isalnum():
      start = idx
      while idx < len(s) and s[idx].isalnum():
        idx += 1
      re = s[start:idx]
      re.reverse()
      s[start:idx] = re
    else:
      idx += 1
print("".join(s))
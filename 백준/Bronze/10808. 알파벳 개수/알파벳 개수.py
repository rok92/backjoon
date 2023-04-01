n = input()
alpha = [0]*26

for i in n:
  alpha[ord(i) - 97] += 1
for i in alpha:
  print(i, end=' ')
  
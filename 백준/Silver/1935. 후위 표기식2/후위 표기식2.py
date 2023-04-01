n = int(input())
cal_form = list(input())
in_num = [int(input()) for i in range(n)]

stack = []
for i in cal_form:
  if i.isalpha():
    stack.append(in_num[ord(i)-65])
  else:
    a = stack.pop()
    b = stack.pop()
    if i == '+':
      b+=a
    elif i == '-':
      b-=a
    elif i == '*':
      b*=a
    elif i == '/':
      b/=a
    stack.append(b)

print("{:.2f}".format(stack[-1]))
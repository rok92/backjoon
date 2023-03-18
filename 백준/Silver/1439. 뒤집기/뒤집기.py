s = input()
zero = s.split('1')
one = s.split('0')
c_zero = 0
c_one = 0
for i in zero:
  if '0' in i:
    c_zero += 1
for i in one:
  if '1' in i:
    c_one += 1
print(min(c_zero, c_one))
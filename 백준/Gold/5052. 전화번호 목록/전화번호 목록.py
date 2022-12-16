import sys

def yOrn(num):
    for i in range(len(num)-1):
      if num[i] == num[i+1][:len(num[i])]:
          print('NO')
          return
    print('YES')

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    num = [str(sys.stdin.readline().strip()) for _ in range(n)]
    num.sort()
    yOrn(num)
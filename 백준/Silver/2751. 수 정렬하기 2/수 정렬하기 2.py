import sys

x = int(sys.stdin.readline())

array = []
for i in range(x) :
    array.append(int(sys.stdin.readline()))
array.sort()

for i in array :
    print(i)
  
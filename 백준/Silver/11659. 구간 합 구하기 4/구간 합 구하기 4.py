import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

sum = 0
sumlist = [0]


for i in num :
    sum += i
    sumlist.append(sum)

for _ in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    ans = sumlist[j] - sumlist[i-1]
    print(ans)
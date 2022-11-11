import sys
input = sys.stdin.readline

N = int(input())
channel = abs(100-N)
M = int(input())
if M :
    broken = set(input().split())
else :
    broken = set()
  

for i in range(1000001) :
    for j in str(i) :
        if j in broken :
            break
    else :
        channel = min(channel, len(str(i)) + abs(i-N))
print(channel)


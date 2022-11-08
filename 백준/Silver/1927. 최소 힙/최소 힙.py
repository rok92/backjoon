import sys
import heapq

N = int(sys.stdin.readline())
array = []
for _ in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if len(array) == 0 :
            print(0)
        else :
            print(heapq.heappop(array))
    else :
        heapq.heappush(array, x)
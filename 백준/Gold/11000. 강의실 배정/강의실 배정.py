import sys
import heapq

input = sys.stdin.readline

N = int(input())

time = [list(map(int, input().split())) for _ in range(N)]
time.sort()

rooms = []
heapq.heappush(rooms, time[0][1])

for i in range(1, N):
    if rooms[0] <= time[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, time[i][1])
print(len(rooms))
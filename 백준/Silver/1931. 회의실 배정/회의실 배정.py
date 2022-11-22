N = int(input())

meeting = []

for i in range(N) :
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key = lambda x : (x[1], x[0]))
end_time = 0
ans = 0
for i in meeting :
    start = i[0]
    end = i[1]
    if start >= end_time :
        ans += 1
        end_time = end
print(ans)

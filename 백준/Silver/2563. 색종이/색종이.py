n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
  x, y = list(map(int, input().split()))

  for row in range(x, x+10):
    for col in range(y, y+10):
      arr[row][col] = 1
answer = 0
for i in arr:
  answer += i.count(1)

print(answer)
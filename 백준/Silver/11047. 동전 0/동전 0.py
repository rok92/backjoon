N, K = map(int, input().split())

coin = []

for i in range(N):
  coin.append(int(input()))

coin.sort(reverse = True)

answer = 0
for x in coin :
    answer += K // x
    K %= x
    if K <= 0:
        break
print(answer)
  
  

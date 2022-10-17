import sys

K, N = list(map(int, sys.stdin.readline().split()))
array = [int(sys.stdin.readline()) for _ in range(K)]

start = 1
end = max(array)

result = 0
while start <= end :
    ttl = 0
    mid = (start + end) // 2
    for i in array :
        ttl += i // mid
    if ttl >= N :
        result = mid
        start = mid + 1
    else : 
        end = mid - 1
print(result)

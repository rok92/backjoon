n, s = map(int, input().split())

a_list = list(map(int, input().split()))

left, right = 0, 0
sum = a_list[0]
length = 100001

while True:
    if sum >= s:
        sum -= a_list[left]
        length = min(length, right-left+1)
        left += 1
    else:
        right += 1
        if right == n:
            break
        sum += a_list[right]
if length == 100001:
    print(0)
else:
    print(length)
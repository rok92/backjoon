n = input()
cnt = [0] * 9
for x in n:
    ind = int(x)
    if ind == 9:
        ind = 6
    cnt[ind] += 1
cnt[6] = (cnt[6]+1) // 2
print(max(cnt))
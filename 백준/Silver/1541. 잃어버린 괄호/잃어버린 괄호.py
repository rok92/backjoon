N = input().split('-')
list = []

for i in N :
    sum = 0
    a = i.split('+')
    for j in a :
        sum += int(j)
    list.append(sum)

answer = list[0]
for i in range(1, len(list)) :
    answer -= list[i]
print(answer)
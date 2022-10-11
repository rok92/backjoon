N = int(input())
rope = []

for i in range(N):
    rope.append(int(input()))
rope.sort(reverse = True)

W = []
for x in range(N) :
    W.append(rope[x] * (x + 1))

print(max(W))
  
triangle = []
for i in range(101) :
    triangle.append(i)
triangle[1] = 1
triangle[2] = 1
triangle[3] = 1
for i in range(4, 101) :
    triangle[i] = triangle[i-3] + triangle[i-2]
T = int(input())
for i in range(T) :
    N = int(input())
    print(triangle[N])
T = int(input())

operation = [300, 60, 10]
real = []
count = 0

if T%10 != 0 :
  print(-1)
else :
  for i in operation:
    count = T // i
    T %= i
    real.append(count)
   
  print(real[0], real[1], real[2])
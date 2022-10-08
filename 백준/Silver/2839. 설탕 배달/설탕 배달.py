sweet = int(input())
bag = 0

while sweet >= 0 : 
    if sweet % 5 == 0 :
        bag += (sweet // 5)
        print(bag)
        break
    sweet -= 3
    bag += 1
else :
    print(-1)
        
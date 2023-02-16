def solution(price, money, count):
    answer = 0
    price_arr = []
    for i in range(1, count + 1):
        price_arr.append(price*i)
    ttl = sum(price_arr)
    if ttl - money > 0:
        answer = ttl - money
    else:
        return 0
    
    return answer
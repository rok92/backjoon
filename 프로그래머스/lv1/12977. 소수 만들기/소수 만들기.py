import itertools

def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0    
    prime = []
    for i in itertools.combinations(nums, 3):
        prime.append(sum(i))
    for i in prime:
        if isPrime(i):
            answer += 1
        else:
            continue

    return answer
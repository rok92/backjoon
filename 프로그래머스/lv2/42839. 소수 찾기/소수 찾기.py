from itertools import permutations

def is_prime(x):
    if x < 2 :
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        p = list(map(''.join, permutations(numbers, i)))
        for j in list(set(p)):
            if int(j) < 2:
                continue
            per = True
            for k in range(2, int(int(j)**0.5)+1):
                if int(j) % k == 0:
                    per = False
                    break
            if per:
                answer.append(int(j))
    return len(set(answer))

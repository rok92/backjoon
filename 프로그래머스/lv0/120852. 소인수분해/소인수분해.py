def solution(n):
    prime_num = []
    answer = list()
    k = 2
    
    while k<=n:
        if n%k == 0:
            prime_num.append(k)
            n = n // k
        else:
            k += 1
    for i in prime_num:
        if i not in answer:
            answer.append(i)
    return answer
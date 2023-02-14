def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        n_sum = 0
        for j in range(i, n + 1):
            n_sum += j
            if n_sum == n:
                answer += 1
            if n_sum > n:
                break
    return answer
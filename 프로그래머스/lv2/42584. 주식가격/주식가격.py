from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        price = q.popleft()
        num = 0
        for i in q:
            num += 1
            if price > i:
                break
        answer.append(num)
    
    return answer
def solution(numbers, k):
    answer = 0
    if len(numbers) < k*2:
        numbers = numbers*((k*2)//len(numbers)+1)
    answer = numbers[(k-1)*2]    
    return answer
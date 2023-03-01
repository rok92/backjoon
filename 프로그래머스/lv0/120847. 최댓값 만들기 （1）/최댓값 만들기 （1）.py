def solution(numbers):
    answer = 0
    numbers.sort(reverse = True)
    for i in range(len(numbers)):
        answer = max(answer, numbers[i]*numbers[i-1])
    return answer
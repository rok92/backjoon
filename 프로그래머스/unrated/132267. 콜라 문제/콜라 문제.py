def solution(a, b, n):
    answer = 0
    while n >= a :
        bot = n % a
        n = (n//a)*b
        answer += n
        n += bot
    return answer
def solution(number):
    answer = 0
    for a in range(len(number)-2):
        for b in range(a+1, len(number)-1):
            for c in range(b+1, len(number)):
                print(number[c])
                if number[a] + number[b] + number[c] == 0:
                    answer += 1
    return answer
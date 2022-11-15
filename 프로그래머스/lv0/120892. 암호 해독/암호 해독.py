def solution(cipher, code):
    answer = []
    for i in range(code, len(cipher) + 1) :
        if i%code == 0 :
            answer.append(cipher[i-1])
    return ''.join(answer)
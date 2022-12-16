def solution(n, words):
    answer = [0, 0]
    use_word = []
    use_word.append(words[0])
    for i in range(1, len(words)):
        if words[i][0] == use_word[-1][-1] and words[i] not in use_word:
            use_word.append(words[i])
        else:
            answer = [(i%n)+1, (i//n)+1]
            break
        
    return answer
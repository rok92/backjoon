def solution(citations):
    answer = 0
    citations.sort()
    for index, citation in enumerate(citations):
        print(citation, index)
        if citation >= len(citations)-index:
            answer = len(citations)-index
            return answer
    return 0
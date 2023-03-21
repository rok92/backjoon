def solution(s):
    a = s.upper()
    if a.count('P') == a.count('Y'):
        return True
    return False
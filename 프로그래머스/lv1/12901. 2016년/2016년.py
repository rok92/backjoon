def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = sum(month[:a-1]) + b-1
    return days[answer%7]
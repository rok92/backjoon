def solution(chicken):
    answer = 0
    while chicken >= 10 :
        dak = chicken // 10
        coupon = chicken % 10
        answer += dak
        chicken = dak + coupon
    return answer
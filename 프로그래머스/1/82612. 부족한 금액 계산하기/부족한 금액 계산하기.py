def solution(price, money, count):
    n = 0
    for i in range(1, count+1):
        n += price * i
    if n - money < 0:
        return 0
    return n - money
def solution(x):
    s = list(str(x))
    num = list(map(int, s))
    return x % sum(num) == 0


def solution(n):
    n = list(str(n))
    n.sort()
    n.reverse()
    n = "".join(n)
    return int(n)
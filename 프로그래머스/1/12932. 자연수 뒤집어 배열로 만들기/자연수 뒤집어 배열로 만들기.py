def solution(n):
    answer = []
    n = list(str(n))
    n.reverse()
    answer = list(map(int, n))
    return answer


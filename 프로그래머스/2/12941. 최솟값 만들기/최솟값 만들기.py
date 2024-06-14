def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    l = list(map(lambda x,y: x*y, A,B))
    answer = sum(l)

    return answer
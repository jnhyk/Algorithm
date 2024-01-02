import sys
input = sys.stdin.readline

from collections import defaultdict

N = int(input())
price = [list(map(int, input().rstrip())) for _ in range(N)]

DP = defaultdict(list)

DP[1] = [[0] * 10 for _ in range(N)]
# DP[x][y][z] = 그림을 소유했던 상황이 x인 상태에서 마지막으로 y가 z원에 그림을 샀을때


def DFS(visit, s, p):
    # visit 그림을 소유했던 사람
    # s 그림을 가지고 있는 사람
    # p 지금 그림 가격
    if DP[visit] == []:
        DP[visit] = [[0] * 10 for _ in range(N)]
    
    if DP[visit][s][p] != 0:
        return DP[visit][s][p]
    
    cnt = 0
    for i in range(N):
        if visit & 1 << i == 0: # vistit에서는 i가 아직 그림을 못만져봄
            if p <= price[s][i]: # p 가격에 s가 i 한테 그림을 팔 수 있음
                cnt = max(cnt, DFS(visit | 1 << i, i, price[s][i]) + 1)
    
    DP[visit][s][p] = cnt
    return cnt

print(DFS(1, 0, 0) + 1)
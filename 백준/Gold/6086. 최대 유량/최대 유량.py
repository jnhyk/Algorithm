h = lambda x: ord(x) - ord('A') if x <= 'Z' else ord(x) - ord('a') + 26
f = [[0] * 52 for _ in range(52)]
c = [[0] * 52 for _ in range(52)]
adj = [set() for _ in range(52)]
S = h('A')
T = h('Z')

def make_flow(prv):
    global S, T
    flow = float('inf')
    cur = T
    while cur != S:
        flow = min(flow, c[prv[cur]][cur] - f[prv[cur]][cur])
        #A->Z 경로에서 가장 작은 용량 선택.
        cur = prv[cur]
    cur = T
    while cur != S:
        f[prv[cur]][cur] += flow
        f[cur][prv[cur]] -= flow
        cur = prv[cur]
    return flow

def bfs():
    global S, T
    prv = [-1] * 52
    que = [S]
    for cur in que:
        for nextt in adj[cur]:
            if c[cur][nextt] > f[cur][nextt] and prv[nextt] < 0:
                que.append(nextt)
                prv[nextt] = cur
                if nextt == T: return make_flow(prv) 
    return -1         #목표(T) 까지 가는 경로가 없으면

N = int(input())
for _ in range(N):
    u, v, C = input().split()
    u, v, C = h(u), h(v), int(C)
    c[u][v] += C
    c[v][u] += C
    adj[u].add(v)
    adj[v].add(u)
total_flow = 0
while True:
    flow = bfs()
    if flow > 0: total_flow += flow
    else: break

print(total_flow)
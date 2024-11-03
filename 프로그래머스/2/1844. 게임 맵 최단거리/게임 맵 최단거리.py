from collections import deque

def solution(maps):
    n = len(maps[0])
    m = len(maps)
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < m and 0 <= nx < n and maps[ny][nx] == 1:
                maps[ny][nx] += maps[y][x]
                q.append((nx, ny))
    
    return -1 if maps[m-1][n-1] == 1 else maps[m-1][n-1]
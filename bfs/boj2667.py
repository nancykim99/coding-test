'''
BOJ2667 : 단지번호붙이기 (S1)

해결 방법 : 
cnt로 bfs를 진행할 때마다, +1를 해서 단지 수 구하기
q에 append 될때마다 +1해서 빌딩 수 구하기
'''
from collections import deque

def bfs(x, y, num):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    building = 1
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni = ti + di
            nj = tj + dj
            if 0 <= ni < n and 0 <= nj < n and map_arr[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = num + 1
                building += 1
    return building

n = int(input())
map_arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
b = []
cnt = 0
for i in range(n):
    for j in range(n):
        if map_arr[i][j] == 1 and not visited[i][j]:
            cnt += 1
            b.append(bfs(i, j, cnt))

b.sort()
print(cnt)
for i in range(cnt):
    print(b[i])
'''
PGM : 네트워크 (LV3)

해결 방법 : 
bfs로 graph를 확인하고, 그 노드를 지나가지 않았다면, bfs 진행
bfs를 진행할 때마다 + 1
'''

from collections import deque

def solution(n, computers):
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if computers[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
    visited = [0] * (n + 1)
    def bfs(start):
        q = deque([start])
        visited[start] = 1
        while q:
            cur = q.popleft()
            for i in graph[cur]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer
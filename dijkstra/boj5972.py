'''
BOJ5972 : 택배 배송 (G5)

해결 방법 : 
다익스트라로 거리 구하기

메모 : 
현서야... 소한테 너무하네...
'''
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def dijkstra(n, graph):
    dist = [float("inf")] * (n + 1) # 거리
    dist[1] = 0 # 거리 초기화
    pq = [(0, 1)]
    while pq:
        # 노드 방문 여부 체크
        current_dist, current_n = heapq.heappop(pq)
        # 이미 처리된 노드는 무시하기 -> 만약 현재 거리가 이미 리스트 값보다 크면, 이미 처리된 노드
        if current_dist > dist[current_n]:
            continue
        # 인접 노드 확인
        for neighbor, weight in graph[current_n]:
            distance = current_dist + weight
            # 더 짧은 경로 발견했다면 업데이트
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist[n]


# 인접리스트
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

ans = dijkstra(n, graph)
print(ans)
# 라이브러리 불러오기
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))

# print(graph)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작노드 집어넣기 (차의 출발점 찾기)
queue = deque()
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            queue.append((i, j))
            break

# 주어진 목적지 2를 다른 걸로 바꾸기?
# ex) 2 -> .
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 2 :
            graph[i][j] = '.' 
            break

# bfs 정의
def bfs() :
    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()

        # 상하좌우 실행
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이면 넘기기
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            # 지나갈 수 있는 길이면 (0)
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            
            # 목적지이면 (2 -> '.')
            if graph[nx][ny] == '.' :
                return graph[x][y]


print(bfs())

from collections import deque

# 노드와 간선의 갯수 입력 받기
n, m = map(int, input().split())

# 각 노드에 연결된 간선 정보를 담기 위한 이차원 배열
graph = [[] for _ in range(n + 1)]

# 진입차수 0으로 초기화
indgree = [0] * (n + 1)

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)  # 정점 a에서 b로 이동가능
  indgree[b] += 1  # 진입차수를 1증가

# 위상 정렬 함수
def topology():
  result = []  # 알고리즘 수행 결과를 담을 리스트
  q = deque()  # 큐 기능을 위한 deque라이브러리 사용

  # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, n+1):
    if indgree[i] == 0:
      q.append(i)

  # 큐가 빌때까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      indgree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indgree[i] == 0:
        q.append(i)
  # 위상 정렬을 수행한 결과 출력
  for i in result:
    print(i, end=' ')

topology()
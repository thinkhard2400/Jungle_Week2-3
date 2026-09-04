from collections import deque

def bfs(graph, start):

    visited = []

    queue = deque()

    queue.append(start)
    visited.append(start)

    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


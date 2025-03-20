from collections import deque
import sys

sys.stdout.reconfigure(encoding='utf-8')

def bfs(graph, start, goal):
    queue = deque([([start], 0)])
    visited = set()
    step = 1

    while queue:
        print(f"Bước {step}: Hàng đợi hiện tại: {list(queue)}")
        path, cost = queue.popleft()
        node = path[-1]
        print(f"  - Đang xét nút: {node}, đường đi hiện tại: {path}, chi phí: {cost}")

        if node == goal:
            print(f"\nTìm thấy đường đi đến {goal} với tổng chi phí {cost}!")
            return path, cost

        if node not in visited:
            visited.add(node)
            print(f"  - Đã đánh dấu {node} là đã thăm")
            for neighbor, weight in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append((new_path, cost + weight))
                print(f"  - Thêm đường đi mới vào hàng đợi: {new_path}, chi phí: {cost + weight}")
        step += 1

    print("\nKhông tìm thấy đường đi đến đích.")
    return None, float('inf')

# Định nghĩa đồ thị dưới dạng danh sách kề với trọng số
graph = {
    'S': [('A', 3), ('B', 1)],
    'A': [('C', 1), ('D', 3), ('G', 4)],
    'B': [('C', 4)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

# Thực hiện BFS từ S đến G
shortest_path, total_cost = bfs(graph, 'S', 'G')
print("\nĐường đi ngắn nhất từ S đến G:", shortest_path)
print("Tổng chi phí:", total_cost)
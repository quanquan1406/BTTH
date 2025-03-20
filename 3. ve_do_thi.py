from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Danh sách kề với trọng số & heuristic (h)
graph = {
    'S': [('A', 3), ('B', 1)],
    'A': [('C', 1), ('D', 3), ('G', 4)],
    'B': [('C', 4)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}
heuristics = {'S': 6, 'A': 3, 'B': 4, 'C': 2, 'D': 2, 'G': 0}

# BFS tìm đường đi ngắn nhất
def bfs(graph, start, goal):
    queue = deque([([start], 0)])
    visited = set()
    steps = []
    step = 1

    while queue:
        print(f"Bước {step}: Hàng đợi hiện tại: {list(queue)}")
        path, cost = queue.popleft()
        node = path[-1]
        print(f"  - Đang xét nút: {node}, đường đi hiện tại: {path}, chi phí: {cost}")
        steps.append(list(path))

        if node == goal:
            print(f"\nTìm thấy đường đi đến {goal} với tổng chi phí {cost}!")
            return path, cost, steps

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
    return None, float('inf'), steps

# Thực hiện BFS từ S đến G
shortest_path, total_cost, steps = bfs(graph, 'S', 'G')

# Vẽ đồ thị với NetworkX
G = nx.DiGraph()
for node, edges in graph.items():
    for neighbor, weight in edges:
        G.add_edge(node, neighbor, weight=weight)

# Cố định vị trí các nút
pos = {
    'S': (0, 2), 'A': (1, 1), 'B': (1, 3),
    'C': (2, 3), 'D': (2, 1), 'G': (3, 2)
}

def update(num):
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='pink', node_size=2000, font_size=12)

    # Hiển thị trọng số cạnh
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

    # Hiển thị heuristic trên các nút
    h_labels = {node: f"h={heuristics[node]}" for node in heuristics}
    nx.draw_networkx_labels(G, {k: (v[0], v[1] - 0.2) for k, v in pos.items()}, labels=h_labels, font_size=10,
                            font_color='black')

    if num < len(steps):
        path_edges = list(zip(steps[num], steps[num][1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5, arrows=True)

ani = animation.FuncAnimation(plt.gcf(), update, frames=len(steps), interval=1000, repeat=False)

plt.title("Graph Representation with BFS Animation")
plt.show()

print("\nĐường đi ngắn nhất từ S đến G:", shortest_path)
print("Tổng chi phí:", total_cost)
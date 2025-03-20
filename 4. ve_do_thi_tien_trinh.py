import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time

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

        if node == goal:
            print(f"\nTìm thấy đường đi đến {goal} với tổng chi phí {cost}!")
            steps.append((path, True))
            return path, cost, steps

        if node not in visited:
            visited.add(node)
            print(f"  - Đã đánh dấu {node} là đã thăm")
            for neighbor, weight in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append((new_path, cost + weight))
                print(f"  - Thêm đường đi mới vào hàng đợi: {new_path}, chi phí: {cost + weight}")
        steps.append((path, False))
        step += 1

    print("\nKhông tìm thấy đường đi đến đích.")
    return None, float('inf'), steps

def draw_graph(graph, steps):
    G = nx.DiGraph()
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = {'S': (0, 2), 'A': (1, 0), 'B': (1, 3), 'C': (2, 3), 'D': (2, 0), 'G': (3, 2)}

    plt.figure(figsize=(8, 5))
    node_colors = {node: 'orange' for node in graph}

    for i, (path, is_final) in enumerate(steps):
        plt.clf()
        for node in path:
            node_colors[node] = 'blue'

        nx.draw(G, pos, with_labels=True, node_color=list(node_colors.values()),
                edge_color='black', node_size=2000, font_size=12, font_color='white')

        edge_labels = {(u, v): w for u, v, w in [(a, b, c) for a in graph for b, c in graph[a]]}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red' if is_final else 'blue', width=2)

        plt.title(f"Bước {i + 1}")
        plt.pause(1)

    plt.show()

graph = {
    'S': [('A', 3), ('B', 1)],
    'A': [('C', 1), ('D', 3), ('G', 4)],
    'B': [('C', 4)],
    'C': [('A', 1), ('B', 4), ('G', 3)],
    'D': [('A', 3), ('G', 2)],
    'G': []
}

path, cost, steps = bfs(graph, 'S', 'G')
draw_graph(graph, steps)
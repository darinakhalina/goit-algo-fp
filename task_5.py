import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, to_rgb


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.base_color = color
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def dfs_traversal(node, base_color, visited=set()):
    if node is not None:
        visited.add(node.id)
        node.color = get_color(base_color, len(visited))
        dfs_traversal(node.left, base_color, visited)
        dfs_traversal(node.right, base_color, visited)


def bfs_traversal(root, base_color, visited=set()):
    if root is not None:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.id not in visited:
                visited.add(node.id)
                node.color = get_color(base_color, len(visited))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


def get_color(base_color, index, step=15):
    rgb_color = to_rgb(base_color)
    lightened_rgb = tuple(min(1.0, c + index * step / 255.0) for c in rgb_color)
    lightened_hex = to_hex(lightened_rgb)
    return lightened_hex


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)
    root.right.right.left = Node(13)
    root.right.right.right = Node(14)

    dfs_traversal(root, root.base_color)
    draw_tree(root)

    bfs_traversal(root, root.base_color)
    draw_tree(root)

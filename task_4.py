import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="lightgreen"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(nodes):
    heap_root = build_heap(nodes)
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    tree = add_edges(heap, heap_root, pos)

    colors = [node[1]["color"] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def heap_sort(iterable, descending=False):
    sign = -1 if descending else 1
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    return [sign * heapq.heappop(h) for _ in range(len(h))]


def build_heap(heap, index=0):
    heap = heap_sort(heap)
    if index < len(heap):
        node = Node(heap[index])
        node.left = build_heap(heap, 2 * index + 1)
        node.right = build_heap(heap, 2 * index + 2)
        return node
    return None


if __name__ == "__main__":
    data = [4, 12, 1, 8, 3, 11, 2, 13, 9, 5, 6, 0, 10, 7, 14]
    draw_heap(data)

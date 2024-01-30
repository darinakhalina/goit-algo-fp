import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, start, end, weight):
        self.vertices[start][end] = weight


def dijkstra(graph, start):
    priority_queue = [(0, start)]
    visited = set()
    shortest_paths = {vertex: float("infinity") for vertex in graph.vertices}
    shortest_paths[start] = 0

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.vertices[current_vertex].items():
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    shortest_paths.pop(start, None)

    return shortest_paths


def draw_graph(graph):
    G = nx.Graph()
    for vertex, edges in graph.vertices.items():
        G.add_node(vertex)
        for neighbor, weight in edges.items():
            G.add_edge(vertex, neighbor, weight=weight)

    random_seed = 42
    pos = nx.spring_layout(G)

    labels = {vertex: str(vertex) for vertex in G.nodes}
    edge_labels = {
        (edge[0], edge[1]): str(graph.vertices[edge[0]][edge[1]]) for edge in G.edges
    }

    nx.draw(G, pos, with_labels=True, labels=labels, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_vertex("H")
g.add_vertex("I")
g.add_vertex("J")

g.add_edge("A", "B", 1)
g.add_edge("B", "C", 2)
g.add_edge("A", "C", 1)
g.add_edge("B", "D", 3)
g.add_edge("C", "E", 4)
g.add_edge("D", "F", 2)
g.add_edge("E", "G", 6)
g.add_edge("F", "H", 4)
g.add_edge("F", "I", 3)
g.add_edge("I", "J", 2)

start_vertex = "A"
shortest_paths = dijkstra(g, start_vertex)

print("Вартість найкоротших шляхів від вершини {}: ".format(start_vertex))
for vertex, distance in shortest_paths.items():
    print("Вершина {}: сумарний час - {}".format(vertex, distance))

draw_graph(g)

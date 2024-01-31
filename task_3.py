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

    pos = nx.spring_layout(G)

    labels = {vertex: str(vertex) for vertex in G.nodes}
    edge_labels = {
        (edge[0], edge[1]): str(graph.vertices[edge[0]][edge[1]]) for edge in G.edges
    }

    nx.draw(
        G,
        pos,
        with_labels=True,
        labels=labels,
        font_weight="normal",
        edge_color="lightgray",
        node_color="lightblue",
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()


g = Graph()
g.add_vertex("Tankopiya")
g.add_vertex("Kharkivskykh Dyvizii")
g.add_vertex("Oleksandrivskyj")
g.add_vertex("Heroiv Kharkova")
g.add_vertex("12-ho Kvitnya")
g.add_vertex("Pavlivska Square")
g.add_vertex("Louis Pasteur")
g.add_vertex("Poltavskyi Shliakh")
g.add_vertex("Sumska")
g.add_vertex("Nauky")

g.add_edge("Tankopiya", "Kharkivskykh Dyvizii", 2)
g.add_edge("Kharkivskykh Dyvizii", "Oleksandrivskyj", 3)
g.add_edge("Tankopiya", "Oleksandrivskyj", 9)
g.add_edge("Kharkivskykh Dyvizii", "Heroiv Kharkova", 3)
g.add_edge("Oleksandrivskyj", "12-ho Kvitnya", 4)
g.add_edge("Heroiv Kharkova", "Pavlivska Square", 14)
g.add_edge("12-ho Kvitnya", "Louis Pasteur", 6)
g.add_edge("Pavlivska Square", "Poltavskyi Shliakh", 5)
g.add_edge("Pavlivska Square", "Sumska", 7)
g.add_edge("Sumska", "Nauky", 4)

start = "Tankopiya"
shortest_paths = dijkstra(g, start)

print("Вартість найкоротших шляхів від вершини {}: ".format(start))
for vertex, distance in shortest_paths.items():
    print("Вершина {}: сумарний час - {}".format(vertex, distance))

draw_graph(g)

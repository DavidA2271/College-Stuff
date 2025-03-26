from GraphGenerator import GraphGenerator


def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    checked = [False] * len(graph)
    path = []
    visited = []

    for _ in range(len(graph)):
        min_dist = float('inf')
    get_dist(graph, start, distances, path, visited)


def get_dist(graph, index, distances, path, visited):
    for i in graph[index]:
        if distances[i[0]] > i[1]:
            distances[i[0]] = i[1]
        if i not in path:
            path.append(i)
    visited.append(index)
    a = None
    try:
        a = path.pop()
    except IndexError:
        pass
    if a is not None:
        get_dist(graph, a, distances, path, visited)


if __name__ == '__main__':
    generator = GraphGenerator(num_nodes=10, num_edges=15, directed=True, weighted=True, spatial=False)
    generator2 = GraphGenerator(num_nodes=10, num_edges=15, directed=False, weighted=True, spatial=False)
    directed_graph = generator.generate_graph()
    undirected_graph = generator2.generate_graph()
    print(directed_graph)
    dijkstra(directed_graph, 0)
    print()
    print()
    print(undirected_graph)
    dijkstra(undirected_graph, 0)
    print()
    print()

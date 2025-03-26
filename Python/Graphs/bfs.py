from GraphGenerator import GraphGenerator


def bfs(graph):
    path = []
    visited = set()
    path.append(0)
    _traverse(graph, path, visited)


def _traverse(graph, path, visited):
    ''' Recursive method that pops the first edge in the list and looks at its edges. '''
    try:
        node = path.pop(0)
    except IndexError:
        print('Path is finished')
        return
    visited.add(node)
    adjacents = graph[node]
    for adj in adjacents:
        if adj not in visited:
            path.append(adj)
            print('Node:', node, '\tAdjacent:', adj)
    _traverse(graph, path, visited)


if __name__ == '__main__':
    generator = GraphGenerator(num_nodes=100, num_edges=500, directed=True, weighted=False, spatial=False)
    generator2 = GraphGenerator(num_nodes=100, num_edges=500, directed=False, weighted=False, spatial=False)
    directed_graph = generator.generate_graph()
    undirected_graph = generator2.generate_graph()
    print(directed_graph)
    bfs(directed_graph)
    print()
    print()
    print(undirected_graph)
    bfs(undirected_graph)
    print()
    print()
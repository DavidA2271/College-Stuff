from GraphGenerator import GraphGenerator


def dfs(graph):
    path = []
    visited = set()
    path.append(0)
    _traverse(graph, path, visited)


def _traverse(graph, path, visited):
    ''' Recursive method that pops the last edge in the list and traverses down it. '''
    try:
        node = path.pop()
    except IndexError:
        print('Path is finished')
        return
    print('Node:', node, '\tAdjacent:', graph[node])
    visited.add(node)
    adjacents = graph[node]
    for adj in adjacents:
        if adj not in visited:
            path.append(adj)
    _traverse(graph, path, visited)


if __name__ == '__main__':
    generator = GraphGenerator(num_nodes=100, num_edges=500, directed=True, weighted=False, spatial=False)
    generator2 = GraphGenerator(num_nodes=100, num_edges=500, directed=False, weighted=False, spatial=False)
    directed_graph = generator.generate_graph()
    undirected_graph = generator2.generate_graph()
    print(directed_graph)
    dfs(directed_graph)
    print()
    print()
    print(undirected_graph)
    dfs(undirected_graph)
    print()
    print()
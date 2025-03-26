import random


def generate_random_graph(num_nodes, num_edges):
    ''' The unmodified code you provided '''
    import networkx as nx
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    possible_edges = [(i, j) for i in range(num_nodes) for j in range(i+1, num_nodes)]
    edges = random.sample(possible_edges, min(num_edges, len(possible_edges)))
    G.add_edges_from(edges)
    return G



ALL_COLORS = ['blue', 'red', 'black', 'green', 'orange', 'pink', 'yellow', 'purple', 'brown', 'white']

def bfs(graph):
    ''' Performs a breadth first search '''
    path = []
    colors = {}
    path.append(0)
    _traverse(graph, path, colors)
    print(colors)
    used = set()
    for k, v in colors.items():
        used.add(v)
    print(f"Used {len(used)} different colors.")


def _traverse(graph, path, colors):
    ''' Recursive method that pops the first edge in the list and looks at its edges. '''
    available = ALL_COLORS.copy()
    try:
        node = path.pop(0)
    except IndexError:
        print('Coloring is finished')
        return
    adjacents = graph[node]
    for adj in adjacents:
        # next to colored node
        if adj in colors.keys():
            if colors[adj] in available:
                # remove color from pool of available colors
                available.remove(colors[adj])
        else: # Hasn't been colored, so hasn't been visited
            path.append(adj)
    # set color to first available color
    colors[node] = available[0]
    _traverse(graph, path, colors)


if __name__ == "__main__":
    num_nodes = 6   # Number of nodes (you can modify this value)
    num_edges = 10  # Number of edges (you can modify this value)
    graph = generate_random_graph(num_nodes, num_edges)
    print("Generated Graph Edges:")
    for edge in graph.edges():
        print(edge)
    bfs(graph)

import random


def generate_random_graph(num_nodes, num_edges):
    ''' Unmodified code you provided '''
    import networkx as nx
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    possible_edges = [(i, j) for i in range(num_nodes) for j in range(i+1, num_nodes)]
    edges = random.sample(possible_edges, min(num_edges, len(possible_edges)))
    G.add_edges_from(edges)
    return G



def find_hamilton(graph):
    ''' I find a Hamiltonian Path by traversing nodes based on the count of edges. '''
    adj_count = {}
    smallest_edge = None
    # first i get a count of how many edges each node has
    for i in range(len(graph)): # node count
        adj = len(graph[i])
        adj_count[i] = adj
        if smallest_edge is None or adj < adj_count[smallest_edge]:
            smallest_edge = i
    path = []
    # I start the path at the node with the least amount of edges
    path.append(smallest_edge)
    reversed = False
    while True:
        adjacents = graph[smallest_edge]
        min_node = None
        # find node with least amount of edges that is connected to previous node
        for n in adjacents:
            if n not in path:
                if min_node is None or adj_count[n] < adj_count[min_node]:
                    min_node = n
        # no connected nodes not on path
        if min_node is None:
            # check from other end of constructed path
            if not reversed:
                path.reverse()
                reversed = True
                smallest_edge = path[-1]
            else:
                # Breaks out if both ends of the path have no connected nodes not on the path
                break
        # Add node to path and continue loop
        else:
            smallest_edge = min_node
            path.append(smallest_edge)
    # has traveled to all nodes
    if len(path) == len(graph):
        return True, path
    else:
        return False, path    


if __name__ == "__main__":
    num_nodes = 6   # Number of nodes (you can modify this value)
    num_edges = 10  # Number of edges (you can modify this value)
    graph = generate_random_graph(num_nodes, num_edges)    
    found, path = find_hamilton(graph)
    print("Generated Graph Edges:")
    for edge in graph.edges():
        print(edge)
    print()
    s = 'Hamiltonian path was '
    if not found:
        s += 'not '
    s += 'found.'
    print(s)
    if found:
        print('Path:')
    else:
        print('Incomplete Path:')
    print(path)
    print()
    print('--------------------------------------')
    print()

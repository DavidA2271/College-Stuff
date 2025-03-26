import bfs
import dfs
import time
from GraphGenerator import GraphGenerator



def test(func, graph):
    print(graph)
    t = time.time()
    func(graph)
    return time.time() - t



if __name__ == '__main__':
    generator = GraphGenerator(num_nodes=100, num_edges=500, directed=True, weighted=False, spatial=False)
    generator2 = GraphGenerator(num_nodes=100, num_edges=500, directed=False, weighted=False, spatial=False)
    directed_graph = generator.generate_graph()
    undirected_graph = generator2.generate_graph()

    generator3 = GraphGenerator(num_nodes=500, num_edges=500, directed=True, weighted=False, spatial=False)
    generator4 = GraphGenerator(num_nodes=500, num_edges=500, directed=False, weighted=False, spatial=False)
    directed_graph2 = generator3.generate_graph()
    undirected_graph2 = generator4.generate_graph()

    t = test(dfs.dfs, directed_graph)
    print('Dfs on directed graph took', t, 'seconds')
    t = test(dfs.dfs, undirected_graph)
    print('Dfs on undirected graph took', t, 'seconds')

    t = test(bfs.bfs, directed_graph)
    print('Bfs on directed graph took', t, 'seconds')
    t = test(bfs.bfs, undirected_graph)
    print('Bfs on undirected graph took', t, 'seconds')

    t = test(dfs.dfs, directed_graph2)
    print('Dfs on directed graph took', t, 'seconds')
    t = test(dfs.dfs, undirected_graph2)
    print('Dfs on undirected graph took', t, 'seconds')

    t = test(bfs.bfs, directed_graph2)
    print('Bfs on directed graph took', t, 'seconds')
    t = test(bfs.bfs, undirected_graph2)
    print('Bfs on undirected graph took', t, 'seconds')
    
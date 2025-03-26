import brute_force
import ant_colony
from GraphGenerator_TSP import GraphGenerator
import time


def test_same_graph():
    generator = GraphGenerator(num_nodes=8, spatial=True)
    graph = generator.generate_graph()

    t = time.time()
    print(brute_force.brute_force(graph))
    time_taken = time.time() - t
    print('Took', time_taken, 'seconds')
    print()

    t = time.time()
    print(ant_colony.ant_colony_optimization(graph, 8, 40))
    time_taken = time.time() - t
    print('Took', time_taken, 'seconds')
    print()


def test_ant_colony(nodes, ants, iterations):
    generator = GraphGenerator(num_nodes=nodes, spatial=True)
    graph = generator.generate_graph()

    t = time.time()
    print(ant_colony.ant_colony_optimization(graph, ants, iterations))
    time_taken = time.time() - t
    print('Took', time_taken, 'seconds')
    print()


# test_same_graph()
# test_ant_colony(100, 50, 100)

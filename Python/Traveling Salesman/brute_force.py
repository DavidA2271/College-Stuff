import math
from itertools import permutations
from GraphGenerator_TSP import GraphGenerator
import time


def brute_force(graph):
    num_nodes = int(math.sqrt(len(graph)))
    num_list = [i for i in range(num_nodes)]
    perms = permutations(num_list)
    shortest_perm = None
    for perm in perms:
        perm_list = list(perm)
        distance = 0
        for i in range(num_nodes):
            start = perm_list[i]
            d = 0
            if i + 1 < num_nodes:
                next = perm_list[i+1]
                d = graph[(start, next)]
                print(start, '->', next, d)
            else:
                next = perm_list[0]
                d = graph[(start, next)]
                print(start, '->', next, d)
            distance += d
        print('Total Distance:', distance)
        print()
        if shortest_perm is None:
            shortest_perm = (perm, distance)
        elif distance < shortest_perm[1]:
            shortest_perm = (perm, distance)
    return shortest_perm


'''
generator = GraphGenerator(num_nodes=8, spatial=True)
graph = generator.generate_graph()
t = time.time()
brute_force(graph)
time_taken = time.time() - t
print('Took', time_taken, 'seconds')
'''


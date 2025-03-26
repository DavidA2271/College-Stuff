from GraphGenerator_TSP import GraphGenerator
import math
import random


def ant_colony_optimization(graph, num_ants, num_iterations):
    num_nodes = int(math.sqrt(len(graph)))
    pheromone_matrix = [ [1] * num_nodes for n in range(num_nodes)]
    spf = None # shortest path found
    for _ in range(num_iterations):
        ant_paths = []
        # create ant paths for each "ant"
        for __ in range(num_ants):
            rand_city = random.randint(0, num_nodes-1)
            path_data = start_journey(graph, rand_city, pheromone_matrix)
            ant_paths.append(path_data)

        shortest_path = None
        # determine shortest path in this iteration
        for p in ant_paths:
            if shortest_path is not None:
                if p[0] < shortest_path[0]:
                    shortest_path = p
            else:
                shortest_path = p
        # update matrix using shortest path this iteration
        pheromone_multiplier = 1/shortest_path[0]
        prev = None
        for i in shortest_path[1]:
            if prev is not None:
                pheromone_matrix[prev][i] += pheromone_multiplier
                pheromone_matrix[i][prev] += pheromone_multiplier
            else:
                prev = i
        # determine if this path is shorter than previous shortest paths
        if spf is not None:
            if shortest_path[0] < spf[0]:
                spf = shortest_path
        else:
            spf = shortest_path
    return spf


def start_journey(graph, start, pheromone_matrix):
    num_nodes = int(math.sqrt(len(graph)))
    visited = [start]
    unvisited = get_unvisited_neighbors(visited, num_nodes)
    total_distance = 0
    current_city = start
    # loop until all cities are visited
    while len(unvisited) > 0:
        probs = get_inverse_distance_probability(graph, current_city, unvisited, pheromone_matrix)
        r_float = random.random()
        closest_prob = 2
        for k in probs.keys():
            if k >= r_float and k < closest_prob:
                closest_prob = k
        total_distance += graph[(current_city, probs[closest_prob])]
        current_city = probs[closest_prob]
        unvisited.remove(current_city)
        visited.append(current_city)
        unvisited = get_unvisited_neighbors(visited, num_nodes)
    # after all cities are visited, return to beginning city
    total_distance += graph[(current_city, start)]
    return (total_distance, visited)


def get_unvisited_neighbors(visited_neighbors, num_nodes):
    unvisited = []
    for i in range(num_nodes):
        if i not in visited_neighbors:
            unvisited.append(i)
    return unvisited


def get_inverse_distance_probability(graph, current_city, unvisited_neighbors, pheromone_matrix):
    probs = {}
    total_dist = 0
    # gets total distance from current city to all connected cities
    for i in unvisited_neighbors:
        total_dist += graph[(current_city, i)]

    # gets the inverse probability
    # shorter paths will have higher probability
    temp_probs = []
    total_prob = 0
    for j in unvisited_neighbors:
        p = (1 - ((total_dist - graph[(current_city, j)]) / total_dist))
        p *= pheromone_matrix[current_city][j]
        total_prob += p
        temp_probs.append((j, p))

    # multiplies probabilities by value in pheromone matrix
    prev_prob = 0
    for k in temp_probs:
        probability = k[1]
        # renormalize so total probability chance is 100%
        real_prob = (probability/total_prob) + prev_prob # I add the previous probability, so the probabilities can "stack" on eachother
        probs[real_prob] = k[0]
        prev_prob = real_prob
    return probs

import random
import math

class GraphGenerator:
    def __init__(self, num_nodes, num_edges, directed=False, weighted=False, spatial=False):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.directed = directed
        self.weighted = weighted
        self.spatial = spatial  # Flag for spatial graphs (for A* heuristic)
        self.node_positions = {}  # Store node coordinates if spatial

    def generate_graph(self):
        graph = {i: [] for i in range(self.num_nodes)}

        # If spatial, generate random coordinates for each node
        if self.spatial:
            self.node_positions = {i: (random.randint(0, 100), random.randint(0, 100)) for i in range(self.num_nodes)}

        edges_added = 0
        while edges_added < self.num_edges:
            u = random.randint(0, self.num_nodes - 1)
            v = random.randint(0, self.num_nodes - 1)
            if u != v and v not in graph[u]:
                weight = random.randint(1, 10) if self.weighted else None
                graph[u].append((v, weight) if self.weighted else v)
                if not self.directed:
                    graph[v].append((u, weight) if self.weighted else u)
                edges_added += 1
        return graph

    def calculate_heuristic(self, node1, node2):
        """Calculate Euclidean distance between two nodes (for A* heuristic)"""
        if not self.spatial:
            raise ValueError("Graph is not spatial. Heuristic cannot be calculated.")
        
        x1, y1 = self.node_positions[node1]
        x2, y2 = self.node_positions[node2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Example usage:
# generator = GraphGenerator(num_nodes=10, num_edges=15, directed=False, weighted=True, spatial=True)
# graph = generator.generate_graph()
# heuristic = generator.calculate_heuristic(0, 5)
# print("Graph:", graph)
# print("Heuristic between node 0 and 5:", heuristic)


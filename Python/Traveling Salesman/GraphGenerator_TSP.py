import random
import math

class GraphGenerator:
    def __init__(self, num_nodes, spatial=True):
        self.num_nodes = num_nodes
        self.spatial = spatial
        self.node_positions = {}  # Store node coordinates if spatial

    def generate_graph(self):
        # If spatial, generate random coordinates for each node (representing cities)
        if self.spatial:
            self.node_positions = {i: (random.randint(0, 100), random.randint(0, 100)) for i in range(self.num_nodes)}

        graph = {}
        for i in range(self.num_nodes):
            graph[i] = {}
            for j in range(i + 1, self.num_nodes):
                distance = self.calculate_distance(i, j)
                graph[i,j] = distance
                graph[j,i] = distance
        return graph

    def calculate_distance(self, node1, node2):
        """Calculate Euclidean distance between two nodes (cities)"""
        x1, y1 = self.node_positions[node1]
        x2, y2 = self.node_positions[node2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Example usage:
# generator = GraphGenerator(num_nodes=10, spatial=True)
# graph = generator.generate_graph()



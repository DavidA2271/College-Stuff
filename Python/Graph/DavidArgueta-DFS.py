import csv
    

class csv_Graph:
    ''' Loads graph from a csv file '''
    def __init__(self, filename):
        self.rows = []
        self.csv_reader(filename)
    def csv_reader(self, filename):
        ''' reads csv and stores its contents in self.rows '''
        with open(filename) as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                self.rows.append(row)
    def csv_to_graph(self):
        ''' returns a Graph constructed using a csv file '''
        graph = Graph()
        for row in self.rows:
            vertex = Vertex(key=row['Vertex'], value=row['Vertex'])
            graph.add(vertex)
            adjacents = row['Adjacents']
            if adjacents is not None:
                adjacents = adjacents.split(',')
                for adj in adjacents:
                    graph.connect(vertex.key, adj)
        return graph


class Vertex:
    ''' Represents one vertex in a graph. Stores a key, a value, and a list of keys of adjacent vertices.'''
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.adjacents = []
    def connect(self, key):
        self.adjacents.append(key)
    def __str__(self) -> str:
        return f'\'Key: {self.key}, Value: {self.value}\''
    def __repr__(self) -> str:
        return self.__str__()


class Graph:
    ''' A graph to represent vertices and their connections. '''
    def __init__(self):
        self.vertices = {}
    def add(self, vertex):
        self.vertices[vertex.key] = vertex            
    def connect(self, vkey1, vkey2):
        vertex1 = self.get(vkey1)
        vertex1.connect(vkey2)
    def get(self, key):
        return self.vertices[key]
    

class Stack:
    def __init__(self) -> None:
        self.stack = []
    def push(self, obj):
        self.stack.append(obj)
    def pop(self):
        x = self.stack.pop(-1)
        return x


class DFS:
    ''' Depth First Search '''
    def __init__(self, graph) -> None:
        self.graph = graph
        self.path = Stack()
        self.visited = set()
    def start(self, start_vertex):
        self.path.push(start_vertex)
        self.traverse()
    def traverse(self):
        ''' Recursive method that pops what is on top of the stack and adds it's adjacents to the stack. '''
        try:
            vertex = self.path.pop()
        except IndexError:
            print('Path is finished')
            return
        print('Vertex:', vertex.value)
        self.visited.add(vertex)
        adjacents = vertex.adjacents
        for adj in adjacents:
            v = graph.get(adj)
            if v not in self.visited:
                self.path.push(v)
        self.traverse()


if __name__ == '__main__':
    reader = csv_Graph('graph_directions.csv')
    graph = reader.csv_to_graph()
    dfs = DFS(graph)
    start_vertex = graph.get('0')
    print('Starting DFS')
    dfs.start(start_vertex)

import re


class BST:
    def __init__(self):
        self.root = None
    def push(self, key, value):
        if self.root is None:
            n = Node()
            n.set_data(key, value)
            self.root = n
        self._add(self.root, key, value)
    def _add(self, c_node, key, value):
        if c_node.key == key:
            c_node.values.add(value)
        elif c_node.key > key:
            if c_node.left is None:
                c_node.left = Node()
                c_node.left.set_data(key, value)
            else:
                self._add(c_node.left, key, value)
        else:
            if c_node.right is None:
                c_node.right = Node()
                c_node.right.set_data(key, value)
            else:
                self._add(c_node.right, key, value)
    def get_node(self, key, c_node=None):
        if c_node is None:
            c_node = self.root
        if c_node.key == key:
            return c_node
        elif c_node.key > key:
            if c_node.left is None:
                return None
            else:
                return self.get_node(key, c_node.left)
        else:
            if c_node.right is None:
                return None
            else:
                return self.get_node(key, c_node.right)


class Node:
    def __init__(self) -> None:
        self.key = None
        self.values = set()
        self.left = None
        self.right = None
    def set_data(self, key, value=None):
        self.key = key
        self.add(value)
    def add(self, value):
        if value is not None:
            #print('Adding to', self.key, 'Line', value)
            self.values.add(value)
    def get_lines(self):
        return sorted(self.values)
    def __str__(self) -> str:
        return f'Key: {self.key}, Lines: {self.get_lines()}'
    

class Indexer:
    def __init__(self) -> None:
        self.bst = BST()
    def index(self, filename):
        l_num = 1
        with open(filename, 'r', encoding='utf-8-sig') as fin:
            for line in fin:
                '''if l_num > 30:
                    return'''
                self._index(line, l_num)
                l_num += 1
    def _index(self, line, l_num):
        token = self.tokenize(line)
        for word in token:
            self.bst.push(word, l_num)
    def tokenize(self, line: str):
        pattern = r'([’\'].(\s|\.)|([\.\!\?\,\-\']))'
        line = line.strip()
        if line == '':
            return []
        line = re.sub(pattern, ' ', line)
        return line.lower().split()
    def get_index(self, key):
        key = key.lower()
        index = self.bst.get_node(key)
        if index is None:
            print(f'The word {key} does not appear in the text.')
        return index

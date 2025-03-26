

class chaining_hashtable:
    def __init__(self, size):
        self.table_size = size
        # creates an 'empty' array of the specified size
        self.table = [None]*self.table_size
    def insert(self, key, value):
        # Normal hash
        key_hash = hash(key)
        # get an index based on size of hash table
        index = self._index(key_hash)
        node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = node
        else:
            # replace head of linked list, resulting in O(1) time
            node.next = self.table[index]
            self.table[index] = node
    def search(self, key):
        key_hash = hash(key)
        index = self._index(key_hash)
        if self.table[index] is not None:
            node = self.table[index]
        else:
            return 'Search: No value associated with the given key'
        if node.key == key:
            return node.value
        else:
            # Traverse list of nodes with the same hash
            while node.next is not None:
                if node.next.key == key:
                    return node.next.value
                else:
                    node = node.next
        return 'Search: No value associated with the given key'
    def delete(self, key):
        key_hash = hash(key)
        index = self._index(key_hash)
        if self.table[index] is not None:
            # replace head if current head was the vaalue to delete
            node = self.table[index]
        else:
            print('Delete: No value associated with the given key')
        if node.key == key:
            self.table[index] = node.next
        else:
            while node.next is not None:
                if node.next.key == key:
                    # skips over desired node, deleting it in the process
                    node.next = node.next.next
                    return
                else:
                    node = node.next
        print('Delete: No value associated with the given key')
    def _index(self, k_hash):
        # makes a hash based off the size of the hash table
        return k_hash % self.table_size
    def __len__(self):
        # traverses through each bucket to count all nodes
        size = 0
        for _ in self.table:
            if _ is not None:
                size += 1
                while _.next is not None:
                    size += 1
                    _ = _.next
        return size


class Node:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value
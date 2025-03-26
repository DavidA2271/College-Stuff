

class double_hash_table:
    def __init__(self, size):
        self.table_size = size
        self.keys = [None]*size
        self.table = [None]*size
        self.max_probe_attempts = int(size/4)
    def insert(self, key, value):
        # Same as linear probe insert aside from index skip
        key_hash = hash(key)
        index = self._index(key_hash)
        counter = 0
        while self.table[index] is not None:
            counter += 1
            if counter > self.max_probe_attempts:
                print('Insert: Cannot insert value, too many collisions')
                return
            # use a second hash to skip
            index += self._double_hash(key_hash)
            if index >= self.table_size:
                index -= self.table_size
        self.keys[index] = key
        self.table[index] = value
    def search(self, key):
        # Same as linear probe search aside from index skip
        key_hash = hash(key)
        index = self._index(key_hash)
        counter = 0
        while self.keys[index] != key:
            counter += 1
            # Since the key would never have been inserted after this many attempts,
            # I can cut off searching after this many attempts as well
            if counter > self.max_probe_attempts:
                return 'Search: Key not found in hash table'
            index += self._double_hash(key_hash)
            if index >= self.table_size:
                index -= self.table_size
        return self.table[index]
    def delete(self, key):
        # Same as linear probe delete aside from index skip
        key_hash = hash(key)
        index = self._index(key_hash)
        counter = 0
        while self.keys[index] != key:
            counter += 1
            # Since the key would never have been inserted after this many attempts,
            # I can cut off searching after this many attempts as well
            if counter > self.max_probe_attempts:
                print('Delete: Key not found in hash table')
                return
            index += self._double_hash(key_hash)
            if index >= self.table_size:
                index -= self.table_size
        self.keys[index] = None
        self.table[index] = None
    def _double_hash(self, key):
        # hash2 implementation
        return (1 + int(key/self.table_size)) % (self.table_size - 1)
    def _index(self, k_hash):
        return k_hash % self.table_size
    def __len__(self):
        size = 0
        for _ in self.table:
            if _ is not None:
                size += 1
        return size
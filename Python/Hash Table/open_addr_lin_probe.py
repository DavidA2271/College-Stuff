

class lin_probe_table:
    def __init__(self, size):
        self.table_size = size
        self.keys = [None]*size
        self.table = [None]*size
        self.max_probe_attempts = int(size/4)
    def insert(self, key, value):
        key_hash = hash(key)
        index = self._index(key_hash)
        counter = 0
        while self.table[index] is not None:
            counter += 1
            if counter > self.max_probe_attempts:
                print('Insert: Cannot insert value, too many collisions')
                return
            index += 1
            if index >= self.table_size:
                index = 0
        self.keys[index] = key
        self.table[index] = value
    def search(self, key):
        key_hash = hash(key)
        index = self._index(key_hash)
        counter = 0
        while self.keys[index] != key:
            counter += 1
            # Since the key would never have been inserted after this many attempts,
            # I can cut off searching after this many attempts as well
            if counter > self.max_probe_attempts:
                return 'Search: Key not found in hash table'
            index += 1
            if index >= self.table_size:
                index = 0
        return self.table[index]
    def delete(self, key):
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
            index += 1
            if index >= self.table_size:
                index = 0
        self.keys[index] = None
        self.table[index] = None
    def _index(self, k_hash):
        return k_hash % self.table_size
    def __len__(self):
        size = 0
        for _ in self.table:
            if _ is not None:
                size += 1
        return size
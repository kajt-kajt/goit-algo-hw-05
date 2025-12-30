class HashTable:
    """
    Hash Table data structure with chaining collision resolution
    """

    def __init__(self, size: int):
        """
        Create new entity of data structure
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        """
        upsert: insert new key-value pair or update existing value
        """
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            # chain for hash value does not exist
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                # if key is already present, than updating value 
                if pair[0] == key:
                    pair[1] = value
                    return True
            # append key-value pair to the end of chain
            self.table[key_hash].append(key_value)
            return True

    def delete(self, key, value = None, ignore_value = False):
        """
        delete key-value pair from table
        Returns False if key-value pair was not found
           and True if found and deleted
        Two modes of work:
        delete(key, ignore_value=True) 
        delete(key, value)
        """
        key_hash = self.hash_function(key)

        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                # if key is already present, than updating value 
                if pair[0] == key and (pair[1] == value or ignore_value):
                    self.table[key_hash].remove(pair)
                    return True
        # chain is empty or key-value pair was not found
        return False

    def get(self, key):
        """
        get value by key
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None



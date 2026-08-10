class LRUCache:
    def __init__(self, capacity: int):
        self.dictionary = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.dictionary:
            return -1
        value = self.dictionary[key]
        self.dictionary.pop(key)
        self.dictionary[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary.pop(key)
        else:
            if len(self.dictionary) == self.capacity:
                first_key = next(iter(self.dictionary))
                self.dictionary.pop(first_key)
        self.dictionary[key] = value

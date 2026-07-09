class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.usage_order = []
        self.max_size = capacity
        self.size = 0
        
        self.lowest_key = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # print(f"put: {key}: value: {value}")
        # Update the value of the key if the key exists
        if key in self.cache:
            self.cache[key] = value
            self.usage_order.remove(key)
            self.usage_order.append(key)

        else:
            # Otherwise, add the key-value pair to the cache. 
            self.cache[key] = value
            self.usage_order.append(key)

            # if not self.lowest_key:
            #     self.lowest_key = key
        
            self.size += 1
            # if the introduction of the new pair causes the cahce to exceed its capacity
            # remove the least recently used key
            if self.size > self.max_size:
                key = self.usage_order.pop(0)
                del self.cache[key]
                # self.lowest_key += 1
                self.size -= 1
            
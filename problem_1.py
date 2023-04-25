from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache:
            return -1
        # Move the accessed item to the end of the cache to denote that it was recently used.
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
        if key is None:
            return

        # If the key is already in the cache, update the value and move it to the end.
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # If the cache is at capacity, remove the least recently used item.
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            # Add the new item to the cache.
            self.cache[key] = value


print("Running tests...")

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print("Expected: 1, Actual:", our_cache.get(1))  # returns 1
print("Expected: 2, Actual:", our_cache.get(2))  # returns 2
# returns -1 because 9 is not present in the cache
print("Expected: -1, Actual:", our_cache.get(9))

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("Expected: -1, Actual:", our_cache.get(3))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("Expected: -1, Actual:", our_cache.get(None))  # returns -1

# Test Case 2
our_cache.set(None, 3)
print("Expected: -1, Actual:", our_cache.get(None))  # returns -1

# Test Case 3
our_cache.set(999999999999999999999999, 3)  # large number
print("Expected: 3, Actual:", our_cache.get(
    999999999999999999999999))  # returns 3

# Test Case 4
# returns -1 because 1 is no longer present
print("Expected: -1, Actual:", our_cache.get(1))

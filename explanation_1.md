# Walkthrough
`OrderedDict` is used as it takes care of maintaining the order of insertion and allows constant-time insertions, deletions, and updates.

# Time Efficiency
1. `get` operation: O(1), because it directly accesses the OrderedDict, which is a hash table with constant time lookup, and the move_to_end operation is also constant time.
2. `set` operation: O(1), as the OrderedDict allows constant-time insertions, deletions, and updates.

# Space Efficiency
O(n), because it uses an OrderedDict to store the cache items, and this data structure has a maximum size of n (the capacity of the cache).
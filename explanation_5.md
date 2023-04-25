# Walkthrough
We use recursion to check all available sub groups.


# Time Efficiency
1. `Block.__init__`: O(1) - Constant time since it initializes a few attributes.
2. `Block.calc_hash`: O(n) - Linear time complexity, where n is the length of the input string (the combination of timestamp, data, and previous_hash). The time complexity is determined by the hashing function.
3. `BlockChain.add_block`: O(1) - Constant time complexity as it involves appending a new block to the tail of the blockchain and updating the connections dictionary.
4. `BlockChain.__iter__`: O(n) - Linear time complexity, where n is the number of blocks in the blockchain. Iterating over the entire blockchain takes linear time.

The most significant time complexity for the given implementation is O(n).

# Space Efficiency
1. `Block class`: O(1) - Constant space complexity since it stores a constant number of attributes for each block (timestamp, data, previous_hash, and hash).
2. `BlockChain` class: O(n) - Linear space complexity, where n is the number of blocks in the blockchain.

The most significant space complexity is O(n).
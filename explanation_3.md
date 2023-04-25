# Walkthrough
A min-heap is used for the priority queue in the Huffman encoding algorithm because it provides an efficient way to maintain and extract the nodes with the minimum frequency values while building the Huffman tree. The main advantage of using a min-heap is its time complexity for the operations needed for this algorithm

# Time Efficiency
- *n* - the number of unique characters in the input string.
- *m* - the length of the input string.

1. Building the Huffman tree:
The time complexity of building the heap is O(n). In each iteration, two nodes are popped (O(log n)) and a new node is pushed back (O(log n)). This step is repeated n-1 times. Therefore, the time complexity of building the Huffman tree is O(n log n).

2. Generating the codes:
The algorithm traverses the entire Huffman tree in a depth-first manner, visiting each node exactly once. The maximum depth of the tree is O(n) for an unbalanced tree and O(log n) for a balanced tree. The time complexity of generating the codes is O(n) in the worst case.

3. Encoding the data:
Each character in the input string is replaced with its corresponding Huffman code. The time complexity of this step is O(m).

4. Decoding the data:
The decoding process traverses the Huffman tree for each bit in the encoded data. The time complexity is O(m).

5. Generating the frequencies table:
This process traverses through each character in the input string and thus takes O(m).

Overall, the time complexity of the entire process (encoding and decoding) is dominated by the **O(n log n)** complexity of building the Huffman tree.

# Space Efficiency
The primary factors are the storage required for the Huffman tree, the code dictionary, and the encoded data. The space complexity is O(n) for the Huffman tree, O(n) for the code dictionary, and O(m) for the encoded data. The overall space complexity is **O(n + m)**.
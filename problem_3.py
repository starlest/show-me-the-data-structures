import sys
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
    def __repr__(self):
        return f"Node({self.char}, {self.freq})"
    
def extract_char_freq(data):
    char_freq = {}
    for char in data:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    return char_freq

def build_huffman_tree(symbols_freq):
    priority_queue = [HuffmanNode(char, freq) for char, freq in symbols_freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_codes(root):
    codes = {}
    stack = []

    if root:
        stack.append((root, ""))

    while stack:
        curr_node, curr_code = stack.pop()

        if curr_node.char is not None:
            codes[curr_node.char] = curr_code
        else:
            if curr_node.left:
                stack.append((curr_node.left, curr_code + "0"))
            if curr_node.right:
                stack.append((curr_node.right, curr_code + "1"))

    return codes
    
def huffman_encoding(data):
    if len(data) == 0:
        return "", None
    
    char_freq = extract_char_freq(data)
    root = build_huffman_tree(char_freq)
    codes = generate_codes(root)
    encoded_data = "".join([codes[char] for char in data])
    return encoded_data, root

def huffman_decoding(data, tree):
    decoded_data = []
    current_node = tree

    for bit in data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree

    return "".join(decoded_data)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
print("Testing...")

def test(test_string):
    encoded_data, tree = huffman_encoding(test_string)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("test_string: ", test_string)
    print("encoded_data: ", encoded_data)
    print("decoded_data: ", decoded_data)
    print("Test: ", "Pass" if test_string == decoded_data else "Fail")
    print()
    
# Test Case 1
print("Test 1")
test_string = "AAAAAAABBBCCCCCCCDDEEEEEE"
test(test_string)

# Test Case 2
print("Test 2")
test_string = ""
test(test_string)

# Test Case 3
print("Test 3")
test_string = "Z XSD SADAS XCZX"
test(test_string)
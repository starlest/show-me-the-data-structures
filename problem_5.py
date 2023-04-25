import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp}-{self.data}-{self.previous_hash}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"Block({self.timestamp}, {self.data}, {self.previous_hash}, {self.hash})"

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        timestamp = datetime.now()
        previous_hash = self.tail.hash if self.tail else '0'
        new_block = Block(timestamp, data, previous_hash)
        if self.tail:
            self.tail.next = new_block
        else:
            self.head = new_block
        self.tail = new_block

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
def test_normal_case():
    # Create a blockchain and add blocks
    blockchain = BlockChain()
    for i in range(3):
        blockchain.add_block(f"Block {i} data")

    # Check if the blocks are connected correctly
    blocks = [block for block in blockchain]
    assert blocks[1].previous_hash == blocks[0].hash, "Error: Blocks not connected correctly"
    assert blocks[2].previous_hash == blocks[1].hash, "Error: Blocks not connected correctly"
    print("Test Normal Case: Passed")

def test_empty_blockchain():
    # Create an empty blockchain
    blockchain = BlockChain()

    # Check if the head and tail are None
    assert blockchain.head is None, "Error: Head should be None"
    assert blockchain.tail is None, "Error: Tail should be None"

    # Check if the blockchain is empty
    assert len(list(blockchain)) == 0, "Error: Blockchain should be empty"
    print("Test Empty Blockchain: Passed")

def test_single_block():
    # Create a blockchain with a single block
    blockchain = BlockChain()
    blockchain.add_block("Block 0 data")

    # Check if the head and tail are the same
    assert blockchain.head is blockchain.tail, "Error: Head and tail should be the same"

    # Check if the blockchain has only one block
    assert len(list(blockchain)) == 1, "Error: Blockchain should have only one block"
    print("Test Single Block: Passed")

if __name__ == "__main__":
    test_normal_case()
    test_empty_blockchain()
    test_single_block()

# import packages
import hashlib # generate hash
from datetime import datetime

# create a block
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.mineVar = 0
        self.hash = self.hash_block()

    def hash_block(self):
        blog_data = str(self.data) + str(self.previous_hash) + str(self.timestamp) + str(self.index ) + str(self.mineVar)
        return hashlib.sha256(blog_data.encode()).hexdigest()
    
    def mine(self):
        while True:
            if self.hash[0:4] == '0000':
                break
            else:
                self.mineVar += 1
                self.hash = self.hash_block()    
    
    def print_info(self):
        print('Index:', self.index)
        print('Timestamp:', self.timestamp)
        print('Data:', self.data)
        print('Previous Hash:', self.previous_hash)
        print('Hash:', self.hash)
        print('MineVar:', self.mineVar)

# create a blockchain
class Blockchain(Block):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0,'Genesis Block', '0'))

    def get_previous_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_previous_block()
        new_block = Block(previous_block.index + 1, data, previous_block.hash)
        new_block.mine()

        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            block.print_info()
            print('-'*50)
    
    def isValid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.hash_block():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


if __name__ == '__main__':
    bac_blockchain = Blockchain()
    bac_blockchain.add_block('Send 1 BTC to Han')
    bac_blockchain.add_block('Send 3 ETH to Ly')
    bac_blockchain.print_chain()
    print('Is blockchain valid?', bac_blockchain.isValid())

    # blockchain.chain[1].data = 'Send 3 more BTC to Ivan'
    bac_blockchain.chain[1].data = 'Send 3 more BTC to Ivan'
    bac_blockchain.print_chain()
    print('Is blockchain valid', bac_blockchain.isValid())

import datetime
from hashlib import sha256

# create the block class that contains the following instance variables: 
# time_stamp as current datetime
# transactions which we will provide
# previous_hash: the prevoius hash of the chain
# nonce: difficulty of the proof of work required to verify, is set at 0
# current blocks hash that is created using the method below
class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

# creates method to create hash using sha256 based on current datetime, transactions, previous hash and nonce. 
# sha256 uses encode to create the hash and uses hexidigest to read hash
    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

# prints out current timedate, transactions, current hash and previous hash
    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash) 
        
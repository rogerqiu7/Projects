# Blockchain Implementation – Use of Object-Oriented Programming to construct a basic blockchain with required proof-of-work

# imports blockchain object from blockchain script
from blockchain import Blockchain

# create blocks and their transactions
block_one_transactions = {"sender":"Roger", "receiver": "John", "amount":"50"}
block_two_transactions = {"sender": "John", "receiver":"Bob", "amount":"30"}
block_three_transactions = {"sender":"Bob", "receiver":"Roger", "amount":"40"}
block_four_transactions = {"sender":"Tucker","receiver":"Simba","amount":"0.2"}

#create a fake transaction
fake_transactions = {"sender": "Roger", "receiver":"Bob", "amount":"100"}

# instantiate a new blockchain object called local blockchain
local_blockchain = Blockchain()

# add the 3 blocks in with their transactions
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.add_block(block_four_transactions)


# print out all the blocks
local_blockchain.print_blocks()
# prints out the genesis block as Block 0, the timestamp, its empty transactions, current hash and previous hash of 0

#local_blockchain.chain[2].transactions = fake_transactions
#local_blockchain.validate_chain()
# print out that current hash does not equal generated hash and validated as False
# current hash will not equal the generated hash because existing block already has a hash
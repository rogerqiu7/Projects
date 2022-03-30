# Blockchain Implementation – Use of Object-Oriented Programming to construct a blockchain with proof-of-work



from blockchain import Blockchain

block_one_transactions = {"sender":"Roger", "receiver": "John", "amount":"50"}
block_two_transactions = {"sender": "John", "receiver":"Bob", "amount":"25"}
block_three_transactions = {"sender":"Bob", "receiver":"Roger", "amount":"35"}
fake_transactions = {"sender": "Roger", "receiver":"John, Bob", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()

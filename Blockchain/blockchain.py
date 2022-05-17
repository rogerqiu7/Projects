# imports block class
from block import Block

# creates the blockchain class that contains the following instance variables: 
# a chain that holds all the blocks inside the blockchain
# unconfirmed transactions that represents all the unverified transactions before being passed into a block.
# a genesis block that is automatically generated when the blockchain is 
class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

# genesis block method automatically creates a genesis block when a new blockchain object is created
# no transactions for genesis block
# use Block class and insert empty transactions and previous hash as 0
# create the hash and append to chain
    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

# add block method adds new blocks to the chain and takes new transactions as arguement
# set previous hash as the hash in the chain list that is its current length minus 1. 
# new block variable uses Block class and inserts new transactions in arguement along with previous hash.
# generates hash based on new transactions, previous hash, datetime, nonce and current hash
# calculates the proof for the block, uses proof of work method far below on new block
# append its to the chain
    def add_block(self, transactions):
        previous_hash = (self.chain[len(self.chain)-1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)

# method prints out contents of the blockchain
# i loops through the entire chain
# current block is the current block being indexed with i.
# print "block" + item number + current block
# print out block contents using print contents method from block
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

# method validates chain by checking to see if all blocks are linked to each other properly
# checks by looping through each of the blocks stored in the blockchain and seeing if previous hash values matches the hash in the previous block
# i loops through entire chain, starts at 1 because 0 is the genesis block
# current is the current block being indexed with i
# previous is the block before that in the chain
# if current hash does not equal generated hash, print out error message and returns false
# if current blocks previous hash does not equal the hash of the previous block, also print out error message and return false
# else, return True for chain has been validated succesfully 
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if(current.hash != current.generate_hash()):
                print("Current hash does not equal generated hash")
                return False
            if(current.previous_hash != previous.generate_hash()):
                print("Previous block's hash got changed")
                return False
        return True

# Proof of work is a security feature in blockchain to prevent attackers from easily taking over the blockchain.
# proof of work method takes block object and a difficulty set at 2
# proof is the generated hash from each block
# while first 2 numbers in proof is not 0 mutliplied by amount of times it appears:
# add 1 to nonce pf the block, generate the hash again and continue until the new proof has 00 infront of it
# block nonce default is 0
# print out the new proof 
    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:2] != "0"*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
      
# Proof of work:
# It makes it difficult for participants to modify blocks by re-calculating hashes.
# It relies on bulletproof cryptography instead of anonymous participants to verify transactions.
# miners need to solve a problem in order to be eligible to broadcast their block. 
# The problem, also known as Proof-of-Work, takes the form of a guessing game that involves the use of hashing.
# Miners first guess a nonce value, which is then combined with the contents of the block (i.e transactions, timestamp, hash, and previous hash). They repeat this process until the desired hash is generated.
# The first miner to produce a proof broadcasts their unconfirmed block together with the correct nonce value. 
# The rest of the network then verifies the calculation. If the majority of the participants agree, the Proof-of-Work for the block is now complete
# Creating an example that demonstrates the difficulty of the math problem that helps protect the blockchain from potential attackers.

# transactions for testing 
new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# import sha256
from hashlib import sha256

# difficulty sets the amount of leading zeros that must be found in the hash produced by the nonce
# currently set at 2, so must have 2 leading 0's
difficulty = 2

# nonce variable with a value of 0. This will be our default starting value.
# this number will continue to be added on until desired proof is found. 
nonce = 0

# creating the proof by adding the nonce along with new transactions
# use encoding method then passing the two strings into the sha256 function.
# uses the .hexdigest() method over the resulting sha256 function to properly store the hash value.
proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()

# printing proof of the new transaction
print("proof: ")
print(proof)
# prints out the hash created by combining nonce and new transactions

# use function that increments the nonce value until the generated hash has difficulty number of leading zeros.
# while first 2 numbers in proof is not 0 mutliplied by amount of times it appears:
# add 1 to nonce and continue until the new proof has 00 infront of it
while (proof[:2] != '0' * difficulty):
  nonce += 1
  proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()

# show the nonce that found the new proof
print("final nonce: ")
print(nonce)

# Once the desired proof has been found, store it in a variable called final_proof and print it out to see the correct hash!
final_proof = proof
print("final proof: ")
print(final_proof)

# If a dishonest participant decides to tamper with a block, they would have to solve the Proof-of-Work for each subsequent block in order to introduce the tampered block into the network. 
# This is computationally infeasible and almost impossible.
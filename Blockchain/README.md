# 🔗 Blockchain Implementation
## Use of Object-Oriented Programming to construct a blockchain with proof-of-work
- First, using OOP to create a block, which will contain a timestamp, transaction, previous hash and current hash
- Then, using OOP to create the blockchain which contains functions to create a genesis block, add blocks, validate the chain based on hashes.
- The blockchain will also contain a proof-of-work which takes the form of a guessing game that involves the use of hashing based on nonce values:

![image](https://user-images.githubusercontent.com/84350865/164949242-59f0c786-d016-46cf-88fb-39ecc52befb5.png)
- Now we create 3 test transactions that should each represent a block in the chain
- When run, we can see the 3 blocks along with the genesis block, each with their timestamp, transactions, current hash and previous hash
![image](https://user-images.githubusercontent.com/84350865/164949144-7b351644-2c62-49e9-ac8a-8ab41f17e77f.png)
- If we add a fake transaction as the 2nd transaction, the blockchain will notice the hash difference and send an alert:
![image](https://user-images.githubusercontent.com/84350865/164949279-c799bf38-e7d4-4499-8328-137c8355d555.png)

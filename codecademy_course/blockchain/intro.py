# Blockchain: A blockchain is an accurate and permanent record of transactions that have been verified and stored in a chronological sequence.
#  The magic of blockchain is that it’s a secure digital ledger that records transactions in chronological order.

# Blocks: A block is an individual transaction or piece of data that is being stored within the blockchain.

# Decentralization: The concept in which users work together to validate transactions without relying on a central authority.

# Participant: A client that owns a copy of the blockchain and verifies transactions across the network.

# Deterministic: The same input will always produce the same output, but that output will never produce the original input.

# Hash: A fixed-length string of a varying combination of letters and numbers produced from a specific input of arbitrary size.

# Hash Function: A function that takes in an input of a random size, performs hashing on this input, 
#   and generates a random output of a fixed size, also known as the hash.

# Genesis Block: The genesis block is the first block on the blockchain and it is typically hard-coded into the blockchain structure. 
#   Being the first block on the blockchain, it does not have a link to a previous hash.
#   Is the most secured block

#Block Properties
# Timestamp: The time the block is created determines the location of it on the blockchain.

# Data: The information to be securely stored in the block.

# Hash: A unique code produced by combining all the contents within the block itself — also known as a digital fingerprint.

# Previous Hash: Each block has a reference to the block prior to its hash. This is what makes the blockchain unique because 
#   this link will be broken if a block is tampered with.

#Adding More Blocks
# As transactions are carried out, they get placed in a special location called the mempool that collects all these unvalidated transactions. 
# The latest transactions in the mempool are broadcasted to all blockchain participants.

# Each participant collects these transactions into a new block. However, each block can only hold a limited number of transactions. 
# Therefore, not all transactions can be added to a block at once.

# Once a block is full, the next set of transactions will have to wait in the memory pool. At this point, the block is said to be unconfirmed, 
# and the transactions inside the block are said to be invalidated.

#How Hashing Maintains the Blockchain's Integrity
# Each block has a unique hash and a link to the previous block’s hash. If a participant decides to tamper with a block by 
#   modifying the transactions, the block’s unique hash gets changed. This results in an invalid copy of the blockchain.

#Proof-of-Work:
# It makes it difficult for participants to modify blocks by re-calculating hashes.
# It relies on bulletproof cryptography instead of anonymous participants to verify transactions.

#Trustless: A feature of blockchain that states how the system doesn’t rely on any participant to verify transactions.

# Miners: Special participants who calculate the Proof-of-Work to mine new blocks.

# Nonce: A number to be guessed by miners which when combined with the block produces an acceptable hash.

# Longest Chain: The most trusted chain with the largest amount of computational work done in calculating the Proof-of-Work.

# Representing Transactions
transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5]

my_transaction = {
  'amount': '500',
  'sender': 'name_1',
  'receiver': 'name_2'
}

mempool.append(my_transaction)

block_transactions = [transaction1, transaction3, my_transaction]
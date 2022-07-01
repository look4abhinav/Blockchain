from Transaction import Transaction
from Block import Block
import hashlib

trx = Transaction('Abhinav','Abhinav',100,10)
genesis_block = Block(trx,'RandomText')
print('Genesis Block')
print(genesis_block.hash,genesis_block.previous_hash)

newtrx = Transaction('Divyam','Abhinav',100,10)
block2 = Block(newtrx,genesis_block.hash)
print('Block 2')
print(block2.hash,block2.previous_hash) 


newtrx = Transaction('Abhinav','Divyam',100,10)
block3 = Block(newtrx,block2.hash)
print('Block 3')
print(block3.hash,block3.previous_hash) 
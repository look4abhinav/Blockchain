import hashlib
from Transaction import Transaction

class Block:
    def __init__(self,transaction,previous_hash):
        self.data = transaction
        self.previous_hash = previous_hash
        data = transaction.getdata() + previous_hash
        self.hash =  hashlib.sha256(data.encode()).hexdigest()
        
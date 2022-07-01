import hashlib
import time

pwd = '1234'
prev = time.time()
hashedpwd = hashlib.sha256(pwd.encode()).hexdigest()
post = time.time()
print("Time taken: ",post-prev)
userpwd = input('Enter password: ')
userpwd = hashlib.sha256(userpwd.encode()).hexdigest()
print(hashedpwd==userpwd)
post = time.time()
print("Time taken: ",post-prev)
import hashlib
result = hashlib.md5(b'MyFirstProject')
  
# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
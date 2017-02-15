from cryptography.fernet import Fernet
# from >filename of encryptor< import cipher_text, key
from Encryption1 import cipher_text, key

# key
cipher_suite = Fernet(key)

# decrypt message with key
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text)

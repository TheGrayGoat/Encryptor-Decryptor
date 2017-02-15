from cryptography.fernet import Fernet
from Encryption1 import cipher_text, key
cipher_suite = Fernet(key)
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text)
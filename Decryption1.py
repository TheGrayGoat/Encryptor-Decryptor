from cryptography.fernet import Fernet
cipher_suite = Fernet(#The key goes here)
plain_text = cipher_suite.decrypt(#The cipher_text goes here)
print(plain_text)

# cryptography can be safely installed by openning a command prompt
# and typing> pip install cryptography
from cryptography.fernet import Fernet

# user enters a message o be encrypted
x = input(str("Enter Message: "))

# is then put into bytes
b = bytes(x, 'utf-8')

# new key generated
key = Fernet.generate_key()

# the key is taken and entered to the text to encrypt it
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b)

print("Key:", key)
print("Encrypted Text:", cipher_text)

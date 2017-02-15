from cryptography.fernet import Fernet

x = input(str("Enter Message: "))

b = bytes(x, 'utf-8')
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"hi")
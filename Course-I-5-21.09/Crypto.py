from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

encrypt_message = f.encrypt(b'IBAN 1111 2222 5555 6666 - Ivan Ivanov')
print(encrypt_message)

decrypt_token = f.decrypt(encrypt_message)
print(decrypt_token)

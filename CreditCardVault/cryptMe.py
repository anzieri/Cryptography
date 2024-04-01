import hashlib
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import customtkinter
import socket  # for socket




class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
    
    def hash(self, text):   
        hashies = sha256(text.encode('utf-8')).hexdigest()
        return hashies

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]
    

def hash(data):   
        hashies = hashlib.sha1(data.encode())
        password = hashies.hexdigest()
        return password




# salt = Random.get_random_bytes(32)
# print(salt)
salt = b'\xc9\xe8\xe1Q\xaf-6\xf9vv\x15\xa7\x89\xa2\xf7$\xad\x1cU\x9c)Mu\xa9\xb0\x13E\xc4\xd3Z?W'
        

    
# Example usage
# password = "mysecretpassword"
# cipher = AESCipher(password)
# encrypted = cipher.encrypt("Hello World")
# print("Encrypted: "+ encrypted)

# decrypted = cipher.decrypt(encrypted)
# print("Decrypted: "+ decrypted)

# print("Hashed value: "+hash("MyCrazyPassword")) # This will remain the same every time you run the code


# Output:
# Encrypted: 3N3uL3bq7JwIzG8y2b7z8A==   # This will change every time you run the code
# Decrypted: Hello World


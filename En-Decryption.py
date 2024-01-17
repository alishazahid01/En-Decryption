#File Encryption and Decryption
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Decorator to greet and print success messages
def print_success(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if "Encryption" in func.__name__:
            print("Encryption is successful!")
        elif "Decryption" in func.__name__:
            print("Decryption is successful!")
        return result
    return wrapper

# Function for generating Cipher and key
def generate_key():
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    return cipher, key, iv

#User validity check 
def valid_user():

    password = int(input("Enter the Password for validity: "))

    #Checking if the password matches or not
    if password == pwd:
        return True
    else:
        return False

# Class for encryption
class Encryption:
    # Constructor
    def __init__(self, plain_text):
        self.plain_text = plain_text

    # Function to perform encryption
    @print_success
    def encrypt_data(self):
        # calling generate_key() to get cipher, key, and iv
        cipher, key, iv = generate_key()
        encryptor = cipher.encryptor()  # Cipher encryptor

        padder = padding.PKCS7(128).padder()  # PKCS7 padding
        padded_data = padder.update(self.plain_text.encode()) + padder.finalize()  # Padding the data

        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        print("Data Encrypted Successfully")

        return encrypted_data, key, iv


# Class for decryption
class Decryption:
    # Constructor
    def __init__(self, pwd:int, encrypted_data, key, iv):
        self.encrypted_data = encrypted_data
        self.pwd = pwd
        self.key = key
        self.iv = iv


    # Function to perform decryption
    @print_success
    def decrypt_data(self):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
        decryptor = cipher.decryptor()  # Cipher decryptor

        Access = valid_user()
        #if Access is valid then decrypt data
        if Access == True:

           decrypted_data = decryptor.update(self.encrypted_data) + decryptor.finalize()
           unpadder = padding.PKCS7(128).unpadder()  # PKCS7 unpadder
           unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()  # Unpadding the data

           print("Decrypted Data:", unpadded_data.decode())
        else:
            print("Inavlid User.....Can't decrypt data")

# input password
pwd = int(input("Enter password: "))

# Reading data from the file
try:
    # try to open the file
    with open("file.txt", "r") as f:
        plain_text = f.read()

except Exception as e:
    print("An exception occurred:", str(e))

encryption_class = Encryption(plain_text)
encrypted_data, key, iv = encryption_class.encrypt_data()

decryption_class = Decryption(pwd, encrypted_data, key, iv)
decryption_class.decrypt_data()

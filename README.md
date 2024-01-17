File Encryption and Decryption Documentation
Introduction

This Python script demonstrates the process of encrypting and decrypting text data using the AES (Advanced Encryption Standard) encryption algorithm in Cipher Block Chaining (CBC) mode. The script allows users to provide a password to access the encrypted data for decryption. This documentation provides an overview of the code structure, usage, and dependencies.
Getting Started

To use the File Encryption and Decryption script, follow these steps:

    Clone or download this repository to your local machine.

    Install the cryptography library, which is required for AES encryption:


pip install cryptography

Create a text file (e.g., file.txt) containing the data you want to encrypt. This script will read the data from this file.

Open the Python script in a code editor and configure the following variables:

    pwd: The password required to access the encrypted data for decryption.
    file.txt: The name of the input file containing the data to be encrypted.

Run the script using the command:


    python encryption_decryption.py

    Follow the prompts to enter the password and perform encryption and decryption.

Code Structure

The File Encryption and Decryption script consists of the following components:
1. Encryption


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

This class is responsible for performing encryption. It takes plain text data as input and uses AES encryption in CBC mode. It also includes padding to ensure data block size consistency.
2. Decryption


class Decryption:
    # Constructor
    def __init__(self, pwd: int, encrypted_data, key, iv):
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
        # if Access is valid then decrypt data
        if Access == True:
           decrypted_data = decryptor.update(self.encrypted_data) + decryptor.finalize()
           unpadder = padding.PKCS7(128).unpadder()  # PKCS7 unpadder
           unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()  # Unpadding the data

           print("Decrypted Data:", unpadded_data.decode())
        else:
            print("Invalid User...Can't decrypt data")

This class is responsible for performing decryption. It takes the encrypted data, password for user validation, and encryption key/IV as inputs. It decrypts the data using the AES algorithm in CBC mode, and user validation is performed to ensure data security.
3. Main Execution

The main part of the script reads data from the input file, encrypts it, and then decrypts it based on user input and validation.
Usage

    Run the Python script to start the encryption and decryption process:


    python encryption_decryption.py

    Enter the password when prompted.

    The script will read the data from the input file (file.txt by default) and encrypt it.

    The encrypted data, along with the encryption key and IV, will be printed.

    To decrypt the data, enter the same password when prompted. The decrypted data will be displayed.

    If an incorrect password is provided during decryption, access to the data will be denied.

Conclusion

This documentation provides an overview of the File Encryption and Decryption script, which allows you to encrypt and decrypt data using the AES encryption algorithm with CBC mode and user validation. You can customize and use this script for securing and accessing sensitive data with password protection.

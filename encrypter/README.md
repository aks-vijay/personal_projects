# Encryption and Decryption for Securing Passwords

This Python script provides a secure implementation of encryption and decryption using the AES-GCM algorithm with PBKDF2HMAC for key derivation. It ensures confidentiality and integrity of data through authenticated encryption.

## Algorithm Used

The script employs the following cryptographic algorithms:

- **Key Derivation Function (KDF):** PBKDF2HMAC with SHA256
- **Symmetric Encryption Algorithm:** AES-GCM (Advanced Encryption Standard in Galois/Counter Mode)
- **Random Initialization Vector (IV):** Generated using a secure random number generator
- **Encoding:** Base64 URL-safe encoding for representation of binary data

## To install it in your machine

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/aks-vijay/personal_projects.git
   cd encrypter

2. **Open the code in PyCharm or any other text editor and enter the below command to bundle the .py file to .exe file:**

   ```bash
   pip install pyinstaller
   pyinstaller --onefile EncryptDecrypt.py
   
# Usage
1. Double click the executable and follow the instructions.
2. The prompt asks whether the user needs to 'encrypt' or 'decrypt'. Enter based on your needs.
3. Enter the salt value: A salt is a random value that is generally not a secret, which is used to make some precomputed attacks harder
4. Enter the seed value: A seed is a random value which generally has to be kept secret or the encryption is broken
5. Enter the plaintext for encryption or cipher text for decryption.

## Prerequisites
1. Before running the script, make sure you have Python installed on your system.
2. Make sure cryptography library is installed in your system

## Features
1. Encryption: Securely encrypt text using PBKDF2 for key derivation and AES in CFB mode for symmetric encryption.
2. Decryption: Decrypt previously encrypted text using the specified salt and seed.

## Security Considerations
1. Ensure that you keep your salt and seed values confidential. Losing them may result in irreversible data loss.
2. The use of PBKDF2HMAC ensures that the key is derived securely from the provided salt and seed.
3. AES-GCM provides both confidentiality and integrity, making the encryption robust against tampering.
4. The script utilizes a secure random number generator for generating the Initialization Vector (IV).

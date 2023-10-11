# Encryption and Decryption for Securing Passwords

This Python script provides a secure implementation of encryption and decryption using the AES-GCM algorithm with PBKDF2HMAC for key derivation. It ensures confidentiality and integrity of data through authenticated encryption.

## Algorithm Used

The script employs the following cryptographic algorithms:

- **Key Derivation Function (KDF):** PBKDF2HMAC with SHA256
- **Symmetric Encryption Algorithm:** AES-GCM (Advanced Encryption Standard in Galois/Counter Mode)
- **Random Initialization Vector (IV):** Generated using a secure random number generator
- **Encoding:** Base64 URL-safe encoding for representation of binary data

## Usage

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/aks-vijay/personal_projects.git


# Usage
## Prerequisites
1. Before running the script, make sure you have Python installed on your system.
2. Make sure cryptography library is installed in your system

## Installation
Clone the repository to your local machine:
> git clone https://github.com/aks-vijay/personal_projects.git
> cd encrypter

## Running the Script
Open a terminal and navigate to the project directory.

## Run the script:
> python encrypt_decrypt.py

Follow the prompts to choose between encryption and decryption, enter the salt and seed, and input the plaintext or ciphertext accordingly.

## Features
Encryption: Securely encrypt text using PBKDF2 for key derivation and AES in CFB mode for symmetric encryption.
Decryption: Decrypt previously encrypted text using the specified salt and seed.

## Security Considerations
Ensure that you keep your salt and seed values confidential. Losing them may result in irreversible data loss.

This script uses the cryptography library, a widely recognized and well-maintained cryptographic library in Python.

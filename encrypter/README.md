# Encryption and Decryption with PBKDF2 and AES

This Python script provides a simple command-line interface for encrypting and decrypting text using the PBKDF2 key derivation function and AES symmetric encryption algorithm. It utilizes the cryptography library for secure key derivation and encryption.

# Usage
## Prerequisites
Before running the script, make sure you have Python installed on your system.

## Installation
Clone the repository to your local machine:
> git clone https://github.com/aks-vijay/personal_projects/encrypter

## Running the Script
Open a terminal and navigate to the project directory.

## Run the script:
python encrypt_decrypt.py

Follow the prompts to choose between encryption and decryption, enter the salt and seed, and input the plaintext or ciphertext accordingly.

## Features
Encryption: Securely encrypt text using PBKDF2 for key derivation and AES in CFB mode for symmetric encryption.
Decryption: Decrypt previously encrypted text using the specified salt and seed.

## Security Considerations
Ensure that you keep your salt and seed values confidential. Losing them may result in irreversible data loss.

This script uses the cryptography library, a widely recognized and well-maintained cryptographic library in Python.

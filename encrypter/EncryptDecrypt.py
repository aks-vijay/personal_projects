import os
from getpass import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode, urlsafe_b64decode


def derive_key(salt, seed):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(seed)
    return key


def encrypt(salt, seed, plaintext):
    key = derive_key(salt, seed)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    tag = encryptor.tag
    encrypted_text = iv + tag + ciphertext
    return urlsafe_b64encode(encrypted_text).decode()


def decrypt(salt, seed, ciphertext):
    key = derive_key(salt, seed)
    data = urlsafe_b64decode(ciphertext.encode())
    iv = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]

    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_bytes = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_bytes.decode()


while True:
    # User input
    choice = input("Do you want to encrypt or decrypt? Enter 'encrypt' or 'decrypt' (type 'exit' to quit): ").lower()

    if choice == 'exit':
        break

    salt = getpass("Enter the salt: ").encode()
    seed = getpass("Enter the seed: ").encode()

    # Perform encryption or decryption based on user input
    if choice == 'encrypt':
        plaintext = input("Enter the plaintext to encrypt: ")
        result = encrypt(salt, seed, plaintext)
        print("Encrypted text:", result)

    elif choice == 'decrypt':
        ciphertext = input("Enter the ciphertext to decrypt: ")
        try:
            result = decrypt(salt, seed, ciphertext)
            print("Decrypted text:", result)
        except Exception as e:
            print("Decryption failed. Make sure the salt and seed are correct.")

    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

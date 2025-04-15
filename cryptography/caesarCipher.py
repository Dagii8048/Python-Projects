"""Encrypt/Decrypt a message using the Caesar cipher.

Args:
    message (str): The message to encrypt/decrypt.
    shift (int): The number of positions to shift each letter.

Returns:
    str: The encrypted/decrypted message.
"""

def caesar_encrypt(message, shift):
    encrypted = ""
    shift = shift % 26
    for char in message:
        if char.isalpha():
            base = 97 if char.islower() else 65
            shifted = (ord(char) - base + shift) % 26
            encrypted += chr(shifted + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(message, shift):
    decrypted = ""
    shift = shift % 26
    for char in message:
        if char.isalpha():
            base = 97 if char.islower() else 65
            shifted = (ord(char) - base -shift) % 26
            decrypted += chr(shifted + base)
        else:
            decrypted += char
    return decrypted

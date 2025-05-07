import random
import string

# Generate a random monoalphabetic cipher key
def generate_monoalphabetic_key():
    letters = list(string.ascii_uppercase)
    shuffled = letters.copy()
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

def inverse_mono_key(mono_key):
    return {v: k for k, v in mono_key.items()}

# Caesar Cipher Function
def caesar_encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char in string.ascii_uppercase:
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Monoalphabetic Substitution Function
def mono_encrypt(text, key):
    return ''.join(key.get(c, c) for c in text.upper())

def mono_decrypt(text, key):
    inverse_key = inverse_mono_key(key)
    return ''.join(inverse_key.get(c, c) for c in text.upper())

# Product Cipher
def product_cipher_encrypt(plaintext, shift, mono_key):
    caesar_text = caesar_encrypt(plaintext, shift)
    final_cipher = mono_encrypt(caesar_text, mono_key)
    return final_cipher

def product_cipher_decrypt(ciphertext, shift, mono_key):
    mono_decrypted = mono_decrypt(ciphertext, mono_key)
    original_text = caesar_decrypt(mono_decrypted, shift)
    return original_text

# Example
shift = 3
mono_key = generate_monoalphabetic_key()

plaintext = "HELLO WORLD"
ciphertext = product_cipher_encrypt(plaintext, shift, mono_key)
decrypted = product_cipher_decrypt(ciphertext, shift, mono_key)

print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted : ", decrypted)
print("Mono Key  : ", mono_key)

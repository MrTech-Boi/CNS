#aes-des
# pip install pycryptodome 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Modes supported: AES.MODE_ECB, CBC, CFB, OFB, CTR
def encrypt_aes(message, key, mode):
    message = message.encode()
    block_size = AES.block_size

    if mode == AES.MODE_ECB:
        cipher = AES.new(key, mode)
        ciphertext = cipher.encrypt(pad(message, block_size))
        return ciphertext, None  # ECB doesn’t use IV

    elif mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]:
        iv = get_random_bytes(block_size)
        cipher = AES.new(key, mode, iv)
        ciphertext = cipher.encrypt(pad(message, block_size))
        return ciphertext, iv

    elif mode == AES.MODE_CTR:
        cipher = AES.new(key, mode)
        ciphertext = cipher.encrypt(message)
        return ciphertext, cipher.nonce

def decrypt_aes(ciphertext, key, mode, iv_or_nonce):
    block_size = AES.block_size

    if mode == AES.MODE_ECB:
        cipher = AES.new(key, mode)
        return unpad(cipher.decrypt(ciphertext), block_size).decode()

    elif mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]:
        cipher = AES.new(key, mode, iv_or_nonce)
        return unpad(cipher.decrypt(ciphertext), block_size).decode()

    elif mode == AES.MODE_CTR:
        cipher = AES.new(key, mode, nonce=iv_or_nonce)
        return cipher.decrypt(ciphertext).decode()

# Example
long_message = "This is a long message that needs secure encryption over multiple blocks." * 2
key = get_random_bytes(16)  # AES-128

modes = {
    "ECB": AES.MODE_ECB,
    "CBC": AES.MODE_CBC,
    "CFB": AES.MODE_CFB,
    "OFB": AES.MODE_OFB,
    "CTR": AES.MODE_CTR
}

for mode_name, mode_val in modes.items():
    print(f"\n--- {mode_name} Mode ---")
    ct, iv = encrypt_aes(long_message, key, mode_val)
    pt = decrypt_aes(ct, key, mode_val, iv)
    print(f"Encrypted (hex): {ct.hex()[:64]}...")
    print(f"Decrypted: {pt[:60]}...")

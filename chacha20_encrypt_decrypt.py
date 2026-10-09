import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

# ChaCha20 is a stream cipher (no padding needed).
# The raw API takes 16 bytes: a 4-byte little-endian block counter
# followed by a 12-byte nonce, as in RFC 7539.

key_bytes = os.urandom(32)  # Fresh key for each standalone demonstration.

nonce_bytes = bytes(4) + os.urandom(12)

chacha20_cipher = Cipher(algorithms.ChaCha20(key_bytes, nonce_bytes), mode=None)
chacha20_encryptor = chacha20_cipher.encryptor()
chacha20_decryptor = chacha20_cipher.decryptor()

plaintext = "someplaintext"
plaintext_bytes = bytes(plaintext, "utf-8")
print("Plaintext: " + plaintext)

ciphertext_bytes = chacha20_encryptor.update(plaintext_bytes) + chacha20_encryptor.finalize()
ciphertext = ciphertext_bytes.hex()
print("Ciphertext: " + ciphertext)

plaintext_bytes_2 = chacha20_decryptor.update(ciphertext_bytes) + chacha20_decryptor.finalize()
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
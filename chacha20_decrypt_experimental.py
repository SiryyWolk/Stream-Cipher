import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

# ChaCha20 is a stream cipher (no padding needed).
# The raw API takes 16 bytes: a 4-byte little-endian block counter
# followed by a 12-byte nonce, as in RFC 7539.

key_bytes = os.urandom(32)  # Fresh key for each standalone demonstration.

nonce_bytes = bytes(4) + os.urandom(12)

chacha20_cipher = Cipher(algorithms.ChaCha20(key_bytes, nonce_bytes), mode=None)
chacha20_encryptor_1 = chacha20_cipher.encryptor()
chacha20_encryptor_2 = chacha20_cipher.encryptor()

plaintext_1 = "someplaintext"
plaintext_bytes_1 = bytes(plaintext_1, "utf-8")
print("Plaintext: " + plaintext_1)

plaintext_2 = "Hi Im Sam potter bridgets"
plaintext_bytes_2 = bytes(plaintext_2, "utf-8")
print("Plaintext: " + plaintext_2)

ciphertext_1_bytes = chacha20_encryptor_1.update(plaintext_bytes_1) + chacha20_encryptor_1.finalize()
ciphertext_1 = ciphertext_1_bytes.hex()
print("Ciphertext: " + ciphertext_1)

ciphertext_2_bytes = chacha20_encryptor_2.update(plaintext_bytes_2) + chacha20_encryptor_2.finalize()
ciphertext_2 = ciphertext_2_bytes.hex()
print("Ciphertext: " + ciphertext_2)

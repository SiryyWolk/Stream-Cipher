from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

# ChaCha20 is a stream cipher (no padding needed).
# The raw API takes 16 bytes: a 4-byte little-endian block counter
# followed by a 12-byte nonce, as in RFC 7539.
key_bytes = bytes("onlyaliceandbobshouldholdthiskey", "utf-8")

nonce_bytes = bytes.fromhex("00000000000000004d2f8a1c93e05b7d")

chacha20_cipher = Cipher(algorithms.ChaCha20(key_bytes, nonce_bytes), mode=None)
chacha20_decryptor = chacha20_cipher.decryptor()



ciphertext = """c2 61 53 2e 6b 9f 23 79
17 c6 ab ce f1 c4 54 e9"""
ciphertext_bytes = bytes.fromhex(ciphertext)
print("Ciphertext: " + ciphertext)

plaintext_bytes_2 = chacha20_decryptor.update(ciphertext_bytes) + chacha20_decryptor.finalize()
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
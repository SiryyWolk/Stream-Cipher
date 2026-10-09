from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

# ChaCha20 is a stream cipher (no padding needed).
# The raw API takes 16 bytes: a 4-byte little-endian block counter
# followed by a 12-byte nonce, as in RFC 7539.
key = "averylongkeymakesforaverygoodkey"
key_bytes = bytes(key, "utf-8")

nonce = "8ec1f037a3f7322e65cf3319a73d0170"
nonce_bytes = bytes.fromhex(nonce)

chacha20_cipher = Cipher(algorithms.ChaCha20(key_bytes, nonce_bytes), mode=None)
chacha20_decryptor = chacha20_cipher.decryptor()



ciphertext = """e8 e7 1b 9c 51 82 d5 07
c6 d1 0f f0 6c 9b 72 07
74 d3 f9 4f f2 32 d3 48
44 f6 e5 94 cf 27 fa ee
36 a8 d1 1d 9d ea cd b4
1d 55 81 ea 1e 7d 1c e2
3b fe fc d0 c9 96 3e aa
e4 12 04 de ee 92 1c d5
b8 c9 21 25 bd 71
"""
ciphertext_bytes = bytes.fromhex(ciphertext)
print("Ciphertext: " + ciphertext)

plaintext_bytes_2 = chacha20_decryptor.update(ciphertext_bytes) + chacha20_decryptor.finalize()
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
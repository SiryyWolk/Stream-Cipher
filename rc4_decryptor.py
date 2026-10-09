from cryptography.hazmat.decrepit.ciphers.algorithms import ARC4
from cryptography.hazmat.primitives.ciphers import Cipher

key = "thisisonelongkey"
key_bytes = bytes(key, "utf-8")
print("Key: " + key)

rc4_cipher = Cipher(ARC4(key_bytes), mode=None)
rc4_decryptor = rc4_cipher.decryptor()

ciphertext = "eb3ec668de7d9e02385544b9691bc38b9d56ab7d9d53e802c186851ad05eadd0972a7556e1962a60a1f6b286bc81114aacbd"
ciphertext_bytes = bytes.fromhex(ciphertext)
print("Ciphertext: " + ciphertext)

plaintext_bytes_2 = rc4_decryptor.update(ciphertext_bytes) + rc4_decryptor.finalize()
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
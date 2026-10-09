from cryptography.hazmat.decrepit.ciphers.algorithms import ARC4
from cryptography.hazmat.primitives.ciphers import Cipher

# RC4 (ARC4) is a stream cipher, now considered broken due to biases in
# its keystream; prohibited in TLS since RFC 7465.

key = "mykey"
key_bytes = bytes(key, "utf-8")
print("Key: " + key)

rc4_cipher = Cipher(ARC4(key_bytes), mode=None)
rc4_encryptor = rc4_cipher.encryptor()
rc4_decryptor = rc4_cipher.decryptor()

plaintext = "someplaintext"
plaintext_bytes = bytes(plaintext, "utf-8")
print("Plaintext: " + plaintext)

ciphertext_bytes = rc4_encryptor.update(plaintext_bytes) + rc4_encryptor.finalize()
ciphertext = ciphertext_bytes.hex()
print("Ciphertext: " + ciphertext)

plaintext_bytes_2 = rc4_decryptor.update(ciphertext_bytes) + rc4_decryptor.finalize()
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)

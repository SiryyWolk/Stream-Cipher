# Stream Cipher Playground

This project is a beginner-friendly collection of Python examples that show how stream ciphers work in practice. I built it to learn the basics of encryption, understand how different ciphers behave, and see how the same idea can be implemented in multiple ways.

A stream cipher encrypts data bit by bit or byte by byte using a keystream. The same keystream is used to decrypt the message, so both sides must share the same key and nonce (when needed).

This repository includes simple demonstrations for:

- RC4
- ChaCha20
- AES in CTR mode

These are educational examples, not production-ready cryptography code.

## Why this project matters

When you are learning cyber security or cryptography, it helps to see the actual code behind the theory. Instead of only reading about encryption, this project shows:

- what a key looks like
- how a nonce is used
- how ciphertext is generated
- how the same process reverses during decryption
- why some older ciphers are considered unsafe

## Project files

- `rc4_decryptor.py` — decrypts a sample RC4 ciphertext using a known key
- `chacha20_decryptor.py` — decrypts a sample ChaCha20 ciphertext
- `chacha20_encrypt_decrypt.py` — generates a fresh ChaCha20 key and nonce, then encrypts and decrypts text
- `aes_ctr_encrypt_decrypt.py` — shows AES in CTR mode, which acts like a stream cipher

## Getting started

Make sure Python is installed, then install the crypto library used in the examples:

```bash
python -m venv .venv
source .venv/bin/activate
pip install cryptography
```

Now run any example:

```bash
python rc4_decryptor.py
python chacha20_decryptor.py
python chacha20_encrypt_decrypt.py
python aes_ctr_encrypt_decrypt.py
```

## Beginner explanation of the concepts

### 1. Stream cipher

A stream cipher creates a pseudo-random stream of bytes from a secret key. It combines that stream with the plaintext to produce ciphertext. Decryption uses the same stream again to recover the original message.

Think of it like this:

```text
ciphertext = plaintext XOR keystream
plaintext = ciphertext XOR keystream
```

The `XOR` operation is the heart of many stream ciphers.

### 2. RC4

RC4 is one of the oldest stream ciphers. It was widely used in the past, but it is now considered insecure and should not be used in modern systems.

This project includes it as a historical example so beginners can see how older ciphers worked and why they were later replaced.

### 3. ChaCha20

ChaCha20 is a modern stream cipher that is much more secure than RC4. It is fast, efficient, and commonly used in real-world systems.

This project demonstrates both:

- decryption with a known key and nonce
- a full encrypt/decrypt example using a fresh key

### 4. AES in CTR mode

AES is normally a block cipher, but in CTR mode it can behave like a stream cipher. Instead of encrypting blocks of the message directly, it encrypts a counter and uses the result as a keystream.

This shows an important idea in cryptography: the same primitive can be used in different modes to support different behaviors.

## What the output looks like

When you run `rc4_decryptor.py`, you should see a plaintext similar to:

```text
You should not use RC4 in real-world applications!
```

That shows the ciphertext can be reversed back into readable text when the correct key is used.

## Important security note

These scripts are designed for learning and experiments. They are not secure enough for real-world production use for several reasons:

- RC4 is broken and deprecated
- fixed keys and sample ciphertexts are used in examples
- nonce and key handling is simplified for readability
- there is no authentication or integrity check

For real applications, use modern authenticated encryption such as:

- AES-GCM
- ChaCha20-Poly1305

## My learning goal

This repository reflects my work as I study cryptography from the ground up. It is meant to be easy for beginners to read, easy to run, and helpful for understanding how stream ciphers work in code.

If you are new to cryptography, start with the smallest file and read the comments carefully. Then try changing the key, nonce, or message and observe what happens.

That is one of the best ways to learn.

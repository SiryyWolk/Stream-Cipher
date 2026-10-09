# Stream Cipher Playground

This repository is a small, beginner-friendly set of Python scripts for exploring how stream ciphers work in practice. It is designed to help someone understand the basics of keystream generation, nonce usage, encryption, and decryption by reading real code instead of only theory.

The project demonstrates several common ciphers and modes:

- RC4
- ChaCha20
- AES in CTR mode

These scripts are meant for learning and experimentation. They are not production-ready cryptography implementations.

## Why this project exists

When learning cryptography, it helps to see:

- what a key and nonce look like in code
- how ciphertext is created from plaintext
- how the same keystream is reused during decryption
- why older ciphers like RC4 are considered unsafe
- how a block cipher can behave like a stream cipher when used in CTR mode

## Repository overview

The project currently contains these examples:

- `rc4_encrypt_decrypt.py` — encrypts and decrypts a short string using RC4/ARC4
- `rc4_decryptor.py` — decrypts a known RC4 ciphertext with a fixed key
- `chacha20_encryptor.py` — decrypts a known ChaCha20 ciphertext using a supplied key and nonce
- `chacha20_encrypt_decrypt.py` — generates a ChaCha20 key/nonce and performs encryption and decryption
- `chacha20_decrypt_experimental.py` — an experimental ChaCha20-oriented script for testing variations
- `aes_ctr_encrypt_decrypt.py` — shows AES in CTR mode, which acts like a stream cipher

## Getting started

Make sure Python is installed, then create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the required dependency:

```bash
pip install cryptography
```

Run any script from the repository root:

```bash
python rc4_encrypt_decrypt.py
python rc4_decryptor.py
python chacha20_encryptor.py
python chacha20_encrypt_decrypt.py
python aes_ctr_encrypt_decrypt.py
```

## Beginner explanation of the concepts

### 1. Stream cipher

A stream cipher generates a pseudo-random keystream from a secret key. That keystream is combined with plaintext to produce ciphertext, and the same keystream is used again during decryption.

The simplest mental model is:

```text
ciphertext = plaintext XOR keystream
plaintext = ciphertext XOR keystream
```

The `XOR` operation is the core idea behind many stream ciphers.

### 2. RC4

RC4 is one of the oldest stream ciphers. It was once widely used, but it is now considered broken and insecure. This repository includes RC4 as a historical example so beginners can see how old implementations behaved and why modern crypto moved away from them.

### 3. ChaCha20

ChaCha20 is a modern stream cipher that is much more secure than RC4. It is fast, efficient, and used in modern cryptographic systems. This project demonstrates both decryption from a fixed example and a simple complete encrypt/decrypt flow.

### 4. AES in CTR mode

AES is normally a block cipher, but in CTR mode it can be used like a stream cipher. Instead of directly encrypting the message, it encrypts a counter value and uses that output as a keystream. This is a good example of how the same primitive can be repurposed for different modes.

## Example output

Running `rc4_decryptor.py` or `rc4_encrypt_decrypt.py` should print values similar to:

```text
Key: mykey
Plaintext: someplaintext
Ciphertext: 6a4d3f...
Original Plaintext: someplaintext
```

This shows the ciphertext can be transformed back into readable text when the same key is used.

## Important security note

These scripts are educational and are intentionally kept simple for readability. They are not appropriate for real-world security use because:

- RC4 is deprecated and broken
- fixed keys and demo ciphertexts are used
- nonce handling is simplified for learning
- there is no authentication or integrity protection

For real applications, use modern authenticated encryption such as:

- AES-GCM
- ChaCha20-Poly1305

## Learning goal

This project is meant to be easy to read, easy to run, and useful for building intuition about how stream ciphers work in code. If you are new to cryptography, start with the smallest script, read the comments carefully, and then modify the key, nonce, or plaintext to see how the output changes.

That hands-on experimentation is usually the fastest way to learn.

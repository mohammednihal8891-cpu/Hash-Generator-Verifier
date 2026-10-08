# Hash Generator & Verifier

A simple Python-based cybersecurity tool that generates and verifies SHA-256 hashes to check file integrity.

## Features

- Generate SHA-256 hash of a file
- Save the original hash
- Verify file integrity
- Detect whether a file has been modified
- Simple menu-based interface

## Technologies Used

- Python 3
- Kali Linux
- SHA-256
- Python hashlib library

## How It Works

1. Select a file and generate its SHA-256 hash.
2. The original hash is saved for future verification.
3. When verification is performed, a new hash is generated.
4. The new hash is compared with the original hash.
5. If both hashes match, the file is considered original.
6. If the hashes are different, the file has been modified.

## How to Run

```bash
python3 hash_tool.py

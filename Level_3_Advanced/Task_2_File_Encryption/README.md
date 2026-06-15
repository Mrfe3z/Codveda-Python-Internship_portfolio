# Task 2: File Encryption

## Overview
A file encryption utility for the Codveda Python Development Internship - Level 3 Advanced tasks.

## Description
This task involves implementing file encryption and decryption using cryptographic algorithms to secure sensitive data.

## Features
- File encryption using industry-standard algorithms
- File decryption with password/key validation
- Support for multiple file types
- Secure key generation
- Error handling and validation
- Progress indication for large files

## Requirements
- Python 3.x
- Libraries: cryptography (or PyCryptodome)

## Usage
```bash
# Encrypt a file
python file_encryption.py encrypt <input_file> <output_file>

# Decrypt a file
python file_encryption.py decrypt <input_file> <output_file>
```

## Structure
- `file_encryption.py` - Main encryption/decryption implementation
- `keys/` - Directory for storing encryption keys (if applicable)

## Learning Objectives
- Understand cryptographic principles
- Learn encryption algorithms (AES, RSA, etc.)
- Implement secure key management
- Handle file I/O with binary data
- Understand security best practices
- Learn password hashing and validation
- Build production-grade security features

## Author
Mrfe3z

## Related
This is part of the [Codveda Python Internship Portfolio](../..)

---
*Task 2 of Level 3 Advanced - Codveda Python Development Internship*

# Technical Report: Web-Based Text Encryption Tool

## Executive Summary

This report provides a comprehensive technical overview of the Web-Based Text Encryption Tool, developed as part of the Information Security course. The application implements multiple encryption algorithms and demonstrates both symmetric and asymmetric cryptographic techniques through an intuitive web interface.

---

## 1. Introduction

### 1.1 Project Objective
The primary goal of this project is to create an educational web application that:
- Demonstrates various encryption and hashing algorithms
- Provides hands-on experience with cryptographic concepts
- Offers a user-friendly interface for encryption/decryption operations
- Implements security best practices in web development

### 1.2 Scope
The application supports six different cryptographic methods:
1. Caesar Cipher (Classical encryption)
2. AES-256 (Modern symmetric encryption)
3. DES (Legacy symmetric encryption)
4. RSA (Asymmetric encryption)
5. Base64 (Encoding)
6. SHA-256 (Cryptographic hashing)

---

## 2. Encryption Techniques Explained

### 2.1 Caesar Cipher

#### Description
The Caesar Cipher is one of the earliest and simplest encryption techniques. It belongs to the substitution cipher family, where each letter in the plaintext is shifted by a fixed number of positions down the alphabet.

#### Implementation Details
- **Algorithm Type**: Symmetric, Substitution Cipher
- **Shift Value**: 3 positions (configurable)
- **Key Size**: N/A (uses shift value)
- **Block Size**: N/A (character-by-character)

#### How It Works
```
Encryption: plaintext_char + shift = ciphertext_char
Decryption: ciphertext_char - shift = plaintext_char
```

**Example:**
- Plaintext: `HELLO`
- Shift: 3
- Ciphertext: `KHOOR`

#### Security Analysis
- **Strengths**: Simple to understand and implement
- **Weaknesses**: 
  - Only 25 possible keys (easily brute-forced)
  - Vulnerable to frequency analysis
  - No practical security in modern context
- **Use Cases**: Educational purposes, basic obfuscation

#### Code Implementation
```python
def caesar_cipher_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result
```

---

### 2.2 AES-256 (Advanced Encryption Standard)

#### Description
AES is a symmetric block cipher established by NIST in 2001 as a replacement for DES. AES-256 uses a 256-bit key, providing the highest level of security in the AES family.

#### Implementation Details
- **Algorithm Type**: Symmetric, Block Cipher
- **Key Size**: 256 bits (32 bytes)
- **Block Size**: 128 bits (16 bytes)
- **Mode**: CBC (Cipher Block Chaining)
- **Padding**: PKCS#7

#### How It Works
1. **Key Generation**: Uses a 256-bit secret key
2. **Initialization Vector (IV)**: Random 16-byte value for CBC mode
3. **Padding**: Adds bytes to make plaintext a multiple of block size
4. **Encryption**: Applies 14 rounds of substitution and permutation
5. **Output Format**: `base64(IV) :: base64(ciphertext)`

#### Security Analysis
- **Strengths**: 
  - Considered unbreakable with current technology
  - Used by governments for classified information
  - Resistant to all known practical attacks
  - 2^256 possible keys (astronomical number)
- **Weaknesses**: 
  - Requires secure key management
  - Vulnerable if key is compromised
- **Use Cases**: 
  - File encryption
  - Database encryption
  - VPNs and secure communications
  - Wireless security (WPA2/WPA3)

#### Code Implementation
```python
def aes_encrypt(text):
    key = b'ThisIsASecretKey' * 2  # 32 bytes for AES-256
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f"{iv}::{ct}"
```

---

### 2.3 DES (Data Encryption Standard)

#### Description
DES was a widely-used symmetric encryption algorithm from 1977 to the early 2000s. It has been officially deprecated due to its small key size.

#### Implementation Details
- **Algorithm Type**: Symmetric, Block Cipher
- **Key Size**: 56 bits (8 bytes, with parity)
- **Block Size**: 64 bits (8 bytes)
- **Mode**: CBC (Cipher Block Chaining)
- **Rounds**: 16

#### How It Works
1. Initial permutation of 64-bit blocks
2. 16 rounds of Feistel network operations
3. Final permutation
4. Uses IV for CBC mode security

#### Security Analysis
- **Strengths**: 
  - Well-studied and understood
  - Fast implementation
- **Weaknesses**: 
  - 56-bit key is too small (brute-force in hours)
  - Vulnerable to differential and linear cryptanalysis
  - Officially deprecated by NIST
- **Use Cases**: 
  - Legacy system support
  - Historical reference
  - Triple-DES (3DES) for enhanced security

#### Code Implementation
```python
def des_encrypt(text):
    key = b'8ByteKey'  # DES requires 8-byte key
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), DES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f"{iv}::{ct}"
```

---

### 2.4 RSA (Rivest-Shamir-Adleman)

#### Description
RSA is an asymmetric cryptographic algorithm that uses a pair of keys: a public key for encryption and a private key for decryption. It's based on the mathematical difficulty of factoring large prime numbers.

#### Implementation Details
- **Algorithm Type**: Asymmetric, Public-Key Cryptography
- **Key Size**: 2048 bits
- **Padding Scheme**: OAEP (Optimal Asymmetric Encryption Padding)
- **Chunk Size**: 190 bytes (safe for 2048-bit key)

#### How It Works
1. **Key Generation**: 
   - Generate two large prime numbers (p, q)
   - Calculate n = p × q
   - Calculate φ(n) = (p-1)(q-1)
   - Choose public exponent e (usually 65537)
   - Calculate private exponent d
2. **Encryption**: C = M^e mod n
3. **Decryption**: M = C^d mod n

#### Security Analysis
- **Strengths**: 
  - Public key can be shared openly
  - Enables digital signatures
  - Secure key exchange
  - Based on hard mathematical problem
- **Weaknesses**: 
  - Slower than symmetric encryption
  - Limited message size
  - Vulnerable if factoring problem is solved (quantum computers)
- **Use Cases**: 
  - SSL/TLS certificates
  - Digital signatures
  - Secure email (PGP)
  - Key exchange protocols

#### Code Implementation
```python
def rsa_encrypt(text):
    cipher = PKCS1_OAEP.new(public_key)
    chunk_size = 190
    encrypted_chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        encrypted_chunk = cipher.encrypt(chunk.encode('utf-8'))
        encrypted_chunks.append(base64.b64encode(encrypted_chunk).decode('utf-8'))
    
    return "||".join(encrypted_chunks)
```

---

### 2.5 Base64 Encoding

#### Description
Base64 is an encoding scheme (not encryption) that converts binary data into ASCII text format using 64 printable characters.

#### Implementation Details
- **Type**: Encoding (reversible, not secure)
- **Character Set**: A-Z, a-z, 0-9, +, /
- **Padding**: = character
- **Expansion**: 33% size increase

#### How It Works
1. Take 3 bytes (24 bits) of input
2. Divide into 4 groups of 6 bits each
3. Map each 6-bit group to Base64 character
4. Add padding if needed

#### Security Analysis
- **Strengths**: 
  - Simple and widely supported
  - Safe for text-based transmission
  - URL and filename safe variants exist
- **Weaknesses**: 
  - Not encryption (easily reversed)
  - No security whatsoever
  - Increases data size
- **Use Cases**: 
  - Email attachments (MIME)
  - Data URLs
  - Storing binary data in JSON/XML
  - Encoding credentials in HTTP headers

---

### 2.6 SHA-256 (Secure Hash Algorithm)

#### Description
SHA-256 is a cryptographic hash function that produces a fixed 256-bit (32-byte) hash value from any input. It's part of the SHA-2 family designed by the NSA.

#### Implementation Details
- **Type**: One-way hash function
- **Output Size**: 256 bits (64 hexadecimal characters)
- **Block Size**: 512 bits
- **Rounds**: 64

#### How It Works
1. Pad message to multiple of 512 bits
2. Parse into 512-bit blocks
3. Process each block through 64 rounds of operations
4. Produce final 256-bit hash

#### Properties
- **Deterministic**: Same input always produces same hash
- **One-way**: Cannot reverse hash to get original input
- **Collision-resistant**: Extremely difficult to find two inputs with same hash
- **Avalanche effect**: Small input change drastically changes hash

#### Security Analysis
- **Strengths**: 
  - Considered cryptographically secure
  - No practical collision attacks known
  - Fast computation
  - Fixed output size
- **Weaknesses**: 
  - Vulnerable to rainbow table attacks (use salt)
  - Not suitable for password storage alone (use bcrypt/argon2)
- **Use Cases**: 
  - Password verification (with salt)
  - Data integrity checking
  - Digital signatures
  - Blockchain and cryptocurrencies
  - Certificate fingerprints

#### Code Implementation
```python
def sha256_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
```

---

## 3. System Architecture

### 3.1 Frontend Architecture

#### HTML Structure
- Semantic HTML5 elements
- Separate tabs for encryption and decryption
- Form elements with proper labels and accessibility
- Output areas with copy functionality

#### CSS Design
- Modern gradient-based color scheme
- Responsive grid layout
- CSS transitions and animations
- Mobile-first approach

#### JavaScript Functionality
- Async/await for API calls
- Event handling and validation
- DOM manipulation
- Clipboard API integration

### 3.2 Backend Architecture

#### Flask Application
- RESTful API endpoints
- JSON request/response format
- CORS enabled for cross-origin requests
- Error handling and validation

#### API Endpoints

**POST /encrypt**
- Request: `{text: string, algorithm: string}`
- Response: `{success: bool, result: string, algorithm: string}`

**POST /decrypt**
- Request: `{text: string, algorithm: string}`
- Response: `{success: bool, result: string, algorithm: string}`

### 3.3 Data Flow

```
User Input → Frontend Validation → API Request → 
Backend Processing → Encryption/Decryption → 
Response → Frontend Display → Copy to Clipboard
```

---

## 4. Security Considerations

### 4.1 Implementation Limitations

**Fixed Keys (Demonstration)**
- Current implementation uses hardcoded keys
- Production systems should use:
  - Environment variables
  - Key management services (KMS)
  - Secure key generation per user/session

**No Data Persistence**
- Application doesn't store user data
- No database required
- Privacy-focused approach

**Session-Based RSA**
- RSA keys generated per server session
- Not per-user (would require authentication)

### 4.2 Best Practices Implemented

1. **Input Validation**
   - Empty input prevention
   - Algorithm selection verification
   - Error handling for invalid inputs

2. **Secure Random Generation**
   - Uses `Crypto.Random.get_random_bytes()` for IVs
   - Cryptographically secure random number generation

3. **Proper Padding**
   - PKCS#7 padding for block ciphers
   - OAEP padding for RSA

4. **Safe Encoding**
   - Base64 encoding for binary data transmission
   - UTF-8 encoding for text

### 4.3 Production Recommendations

For deploying this application in production:

1. **HTTPS/TLS**: Encrypt all data in transit
2. **Key Management**: Use proper key storage and rotation
3. **Authentication**: Implement user authentication
4. **Rate Limiting**: Prevent abuse and DoS attacks
5. **Input Sanitization**: Protect against injection attacks
6. **Logging**: Implement security audit logs
7. **CSP Headers**: Content Security Policy
8. **HSTS**: HTTP Strict Transport Security

---

## 5. Testing and Validation

### 5.1 Test Cases

#### Caesar Cipher
- Plaintext: "Hello World"
- Expected: "Khoor Zruog"
- Decryption: "Hello World"

#### AES-256
- Encryption produces different output each time (random IV)
- Decryption correctly recovers plaintext
- Handles special characters and unicode

#### RSA
- Large text chunking works correctly
- Encryption/decryption cycle maintains data integrity

#### SHA-256
- Produces consistent hash for same input
- Cannot be decrypted (one-way)

### 5.2 Edge Cases Handled

- Empty input validation
- Special characters and unicode
- Very long text (RSA chunking)
- Missing algorithm selection
- Invalid encrypted text format

---

## 6. Conclusion

### 6.1 Project Achievements

This Web-Based Text Encryption Tool successfully:
- ✅ Implements 6 different cryptographic methods
- ✅ Provides intuitive user interface
- ✅ Includes all bonus features
- ✅ Demonstrates security best practices
- ✅ Serves as educational resource

### 6.2 Learning Outcomes

Through this project, the following concepts were explored:
1. **Symmetric vs Asymmetric Encryption**
2. **Block Ciphers and Modes of Operation**
3. **Cryptographic Hashing**
4. **Encoding vs Encryption**
5. **Key Management Principles**
6. **Security Best Practices**

### 6.3 Future Improvements

Potential enhancements:
- User authentication and session management
- Database storage for encrypted messages
- File encryption/decryption
- Custom key input
- Additional algorithms (Blowfish, Twofish)
- Password strength meter
- Encryption performance metrics

---

## 7. References

1. **NIST FIPS 197**: Advanced Encryption Standard (AES)
2. **RFC 3447**: RSA Cryptography Specifications
3. **NIST FIPS 180-4**: SHA-2 Hash Functions
4. **Flask Documentation**: https://flask.palletsprojects.com/
5. **PyCryptodome Documentation**: https://pycryptodome.readthedocs.io/
6. **MDN Web Docs**: Web Cryptography Resources

---

## Appendix A: Installation and Usage

See README.md for complete installation and usage instructions.

---

**Report Prepared By**: Information Security Student  
**Date**: October 2025  
**Course**: Information Security  
**Project**: Web-Based Text Encryption Tool


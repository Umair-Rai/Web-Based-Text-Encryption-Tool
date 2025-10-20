from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import base64
import hashlib
from Crypto.Cipher import AES, DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

app = Flask(__name__)
CORS(app)

# Generate RSA keys for the session
rsa_key = RSA.generate(2048)
public_key = rsa_key.publickey()

# Caesar Cipher Implementation
def caesar_cipher_encrypt(text, shift=3):
    """Encrypt text using Caesar Cipher with given shift"""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift=3):
    """Decrypt text using Caesar Cipher with given shift"""
    return caesar_cipher_encrypt(text, -shift)

# AES Encryption Implementation
def aes_encrypt(text):
    """Encrypt text using AES-256"""
    key = b'ThisIsASecretKey' * 2  # 32 bytes for AES-256
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f"{iv}::{ct}"

def aes_decrypt(encrypted_text):
    """Decrypt text using AES-256"""
    try:
        key = b'ThisIsASecretKey' * 2
        iv, ct = encrypted_text.split('::')
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')
    except Exception as e:
        return f"Decryption Error: {str(e)}"

# DES Encryption Implementation
def des_encrypt(text):
    """Encrypt text using DES"""
    key = b'8ByteKey'  # DES requires 8-byte key
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), DES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f"{iv}::{ct}"

def des_decrypt(encrypted_text):
    """Decrypt text using DES"""
    try:
        key = b'8ByteKey'
        iv, ct = encrypted_text.split('::')
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = DES.new(key, DES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), DES.block_size)
        return pt.decode('utf-8')
    except Exception as e:
        return f"Decryption Error: {str(e)}"

# RSA Encryption Implementation
def rsa_encrypt(text):
    """Encrypt text using RSA"""
    cipher = PKCS1_OAEP.new(public_key)
    # RSA can only encrypt data smaller than key size, so we chunk it
    chunk_size = 190  # Safe size for 2048-bit key
    encrypted_chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        encrypted_chunk = cipher.encrypt(chunk.encode('utf-8'))
        encrypted_chunks.append(base64.b64encode(encrypted_chunk).decode('utf-8'))
    
    return "||".join(encrypted_chunks)

def rsa_decrypt(encrypted_text):
    """Decrypt text using RSA"""
    try:
        cipher = PKCS1_OAEP.new(rsa_key)
        encrypted_chunks = encrypted_text.split("||")
        decrypted_chunks = []
        
        for chunk in encrypted_chunks:
            encrypted_chunk = base64.b64decode(chunk)
            decrypted_chunk = cipher.decrypt(encrypted_chunk)
            decrypted_chunks.append(decrypted_chunk.decode('utf-8'))
        
        return "".join(decrypted_chunks)
    except Exception as e:
        return f"Decryption Error: {str(e)}"

# Base64 Encoding
def base64_encode(text):
    """Encode text using Base64"""
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def base64_decode(text):
    """Decode text using Base64"""
    try:
        return base64.b64decode(text.encode('utf-8')).decode('utf-8')
    except Exception as e:
        return f"Decoding Error: {str(e)}"

# SHA-256 Hashing
def sha256_hash(text):
    """Generate SHA-256 hash"""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """Handle encryption requests"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        algorithm = data.get('algorithm', '')
        
        # Validation
        if not text:
            return jsonify({'error': 'Please enter text to encrypt'}), 400
        
        if not algorithm:
            return jsonify({'error': 'Please select an encryption algorithm'}), 400
        
        # Perform encryption based on selected algorithm
        if algorithm == 'caesar':
            result = caesar_cipher_encrypt(text)
        elif algorithm == 'aes':
            result = aes_encrypt(text)
        elif algorithm == 'des':
            result = des_encrypt(text)
        elif algorithm == 'rsa':
            result = rsa_encrypt(text)
        elif algorithm == 'base64':
            result = base64_encode(text)
        elif algorithm == 'sha256':
            result = sha256_hash(text)
        else:
            return jsonify({'error': 'Invalid algorithm selected'}), 400
        
        return jsonify({
            'success': True,
            'result': result,
            'algorithm': algorithm
        })
    
    except Exception as e:
        return jsonify({'error': f'Encryption failed: {str(e)}'}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    """Handle decryption requests"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        algorithm = data.get('algorithm', '')
        
        # Validation
        if not text:
            return jsonify({'error': 'Please enter text to decrypt'}), 400
        
        if not algorithm:
            return jsonify({'error': 'Please select a decryption algorithm'}), 400
        
        # SHA-256 cannot be decrypted
        if algorithm == 'sha256':
            return jsonify({'error': 'SHA-256 is a one-way hash and cannot be decrypted'}), 400
        
        # Perform decryption based on selected algorithm
        if algorithm == 'caesar':
            result = caesar_cipher_decrypt(text)
        elif algorithm == 'aes':
            result = aes_decrypt(text)
        elif algorithm == 'des':
            result = des_decrypt(text)
        elif algorithm == 'rsa':
            result = rsa_decrypt(text)
        elif algorithm == 'base64':
            result = base64_decode(text)
        else:
            return jsonify({'error': 'Invalid algorithm selected'}), 400
        
        return jsonify({
            'success': True,
            'result': result,
            'algorithm': algorithm
        })
    
    except Exception as e:
        return jsonify({'error': f'Decryption failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)


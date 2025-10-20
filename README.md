# Web-Based Text Encryption Tool

A comprehensive single-page web application that allows users to encrypt and decrypt text using various encryption algorithms. This project demonstrates the implementation of multiple cryptographic techniques with a modern, user-friendly interface.

## 🎯 Project Overview

This web-based encryption tool enables users to:
- Encrypt plaintext using multiple algorithms
- Decrypt ciphertext back to plaintext
- Copy encrypted/decrypted text with one click
- Generate cryptographic hashes
- Learn about different encryption methods

## ✨ Features

### Core Features
- **Multiple Encryption Algorithms**:
  - Caesar Cipher (Classical substitution cipher)
  - AES-256 (Advanced Encryption Standard)
  - DES (Data Encryption Standard)
  - RSA (Public-key cryptography)
  - Base64 (Encoding/Decoding)
  - SHA-256 (Cryptographic hashing)

- **User Interface**:
  - Clean, modern, and responsive design
  - Separate tabs for encryption and decryption
  - Real-time input validation
  - Error handling with user-friendly messages

### Bonus Features ✓
- ✅ **Decryption Feature**: Full support for decrypting encrypted messages
- ✅ **Hashing Option**: SHA-256 hash generation
- ✅ **Copy Functionality**: One-click copy to clipboard for results
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile devices

## 🛠️ Technology Stack

### Frontend
- **HTML5**: Structure and semantic markup
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript (ES6+)**: Client-side interactivity and API communication

### Backend
- **Python 3.x**: Server-side logic
- **Flask**: Lightweight web framework
- **Flask-CORS**: Cross-Origin Resource Sharing support

### Encryption Libraries
- **PyCryptodome**: Comprehensive cryptography library
  - AES encryption/decryption
  - DES encryption/decryption
  - RSA public-key cryptography
- **hashlib**: SHA-256 hashing (Python built-in)
- **base64**: Base64 encoding/decoding (Python built-in)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd Web-Based-Text-Encryption-Tool
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to: `http://localhost:5000`

## 🔐 Encryption Algorithms Explained

### 1. Caesar Cipher
- **Type**: Symmetric, Classical
- **Description**: Shifts each letter in the plaintext by a fixed number of positions (default: 3)
- **Use Case**: Educational purposes, simple obfuscation
- **Strength**: Very weak, easily breakable

### 2. AES-256 (Advanced Encryption Standard)
- **Type**: Symmetric, Block cipher
- **Description**: Industry-standard encryption using 256-bit keys
- **Use Case**: Secure data storage, file encryption, VPNs
- **Strength**: Very strong, considered unbreakable with current technology

### 3. DES (Data Encryption Standard)
- **Type**: Symmetric, Block cipher
- **Description**: Legacy encryption algorithm with 56-bit keys
- **Use Case**: Historical significance, legacy system support
- **Strength**: Weak by modern standards, vulnerable to brute-force attacks

### 4. RSA (Rivest-Shamir-Adleman)
- **Type**: Asymmetric, Public-key cryptography
- **Description**: Uses public/private key pair for encryption (2048-bit)
- **Use Case**: Digital signatures, secure key exchange, SSL/TLS
- **Strength**: Strong, computational difficulty of factoring large numbers

### 5. Base64
- **Type**: Encoding (not encryption)
- **Description**: Encodes binary data in ASCII string format
- **Use Case**: Data transmission, email attachments, URLs
- **Strength**: Not secure, easily reversible

### 6. SHA-256
- **Type**: One-way hash function
- **Description**: Generates a 256-bit fixed-size hash
- **Use Case**: Password storage, data integrity verification, blockchain
- **Strength**: Cannot be reversed, collision-resistant

## 💡 Usage Guide

### Encrypting Text
1. Select the **Encrypt** tab
2. Enter your plaintext in the text area
3. Choose an encryption algorithm from the dropdown
4. Click **Encrypt Text**
5. View the encrypted result in the output area
6. Click the 📋 button to copy the result

### Decrypting Text
1. Select the **Decrypt** tab
2. Paste or enter the encrypted text
3. Choose the same algorithm used for encryption
4. Click **Decrypt Text**
5. View the decrypted plaintext
6. Click the 📋 button to copy the result

### Keyboard Shortcuts
- **Ctrl/Cmd + Enter**: Trigger encrypt/decrypt action

## 🔒 Security Considerations

### Important Notes
1. **Fixed Keys**: This implementation uses fixed encryption keys for demonstration purposes. In production, keys should be:
   - Randomly generated
   - Securely stored (environment variables, key management systems)
   - Never hardcoded in source code

2. **Session-Based RSA**: RSA keys are generated per server session, not per user

3. **No Data Persistence**: This application does not store any user data

4. **Educational Purpose**: This tool is designed for learning and demonstration. For production use:
   - Implement proper key management
   - Use HTTPS/TLS for data transmission
   - Add user authentication and authorization
   - Implement rate limiting and input sanitization

## 🎨 User Interface Features

- **Modern Gradient Design**: Purple gradient theme with smooth transitions
- **Responsive Layout**: Adapts to different screen sizes
- **Tab Navigation**: Clean separation between encrypt and decrypt functions
- **Visual Feedback**: 
  - Success/error messages
  - Copy button animation
  - Form validation indicators
- **Information Section**: Educational cards explaining each algorithm

## 📊 Project Structure

```
Web-Based-Text-Encryption-Tool/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/
│   └── index.html        # Main HTML page
└── static/
    ├── style.css         # CSS styling
    └── script.js         # JavaScript functionality
```

## 🧪 Testing the Application

### Test Cases

1. **Caesar Cipher**
   - Input: `Hello World`
   - Output: `Khoor Zruog`

2. **Base64**
   - Input: `Secret Message`
   - Output: `U2VjcmV0IE1lc3NhZ2U=`

3. **SHA-256**
   - Input: `password123`
   - Output: `ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f`

4. **AES-256**
   - Input: `Confidential Data`
   - Output: Random encrypted string (changes each time)

## 🚀 Future Enhancements

Potential improvements for the project:
- [ ] User authentication system
- [ ] Save encrypted messages to database
- [ ] File encryption/decryption support
- [ ] Custom key input for algorithms
- [ ] Export encryption history
- [ ] Multi-language support
- [ ] Dark mode toggle
- [ ] Encryption strength indicator
- [ ] QR code generation for encrypted text

## 📝 Assignment Compliance

This project fulfills all requirements:

### Core Requirements ✓
- [x] Text box for plain text input
- [x] Dropdown menu for algorithm selection
- [x] Encryption button
- [x] Text area for ciphertext display
- [x] At least 3 encryption algorithms (6 implemented)
- [x] Proper handling of different encryption methods
- [x] Input validation (empty inputs, algorithm selection)

### Bonus Features ✓
- [x] Decryption feature
- [x] Hashing option (SHA-256)
- [x] Copy ciphertext functionality
- [ ] User authentication (optional, not implemented)

## 👨‍💻 Development

### Running in Development Mode
```bash
python app.py
```
The server will run on `http://localhost:5000` with debug mode enabled.

### Dependencies
See `requirements.txt` for complete list:
- Flask 3.0.0
- flask-cors 4.0.0
- pycryptodome 3.19.0

## 📄 License

This project is developed for educational purposes as part of an Information Security course assignment.

## 🙏 Acknowledgments

- **Flask Documentation**: Web framework guidance
- **PyCryptodome**: Comprehensive cryptography library
- **MDN Web Docs**: Frontend development resources

## 📞 Support

For issues or questions:
1. Check the README documentation
2. Review the code comments
3. Test with the provided test cases
4. Verify all dependencies are installed

---

**Note**: This application is designed for educational and demonstration purposes. Always use proper security practices in production environments.


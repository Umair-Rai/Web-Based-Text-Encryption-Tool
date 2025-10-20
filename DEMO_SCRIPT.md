# Demo Video Script

## Web-Based Text Encryption Tool - Demonstration

---

### Introduction (30 seconds)

"Hello! Today I'm demonstrating the Web-Based Text Encryption Tool, a comprehensive web application that showcases various encryption and hashing algorithms. This project implements 6 different cryptographic methods with a modern, user-friendly interface."

---

### Application Overview (30 seconds)

**[Show the homepage]**

"As you can see, the application features a clean, modern interface with a purple gradient design. We have two main tabs:
- Encrypt: For encrypting plaintext
- Decrypt: For decrypting ciphertext

Below, there's an information section explaining each supported algorithm."

---

### Demonstration 1: Caesar Cipher (1 minute)

**[Click on Encrypt tab]**

"Let's start with the classic Caesar Cipher. I'll enter the text 'Hello World'"

**[Type in plaintext]**
- Input: `Hello World`

**[Select Caesar Cipher from dropdown]**

"Now I select Caesar Cipher from the dropdown menu, which uses a shift of 3 positions."

**[Click Encrypt button]**

"And click Encrypt. As you can see, the ciphertext is now 'Khoor Zruog' - each letter has been shifted 3 positions forward in the alphabet."

**[Click copy button]**

"I can easily copy this to clipboard with one click."

**[Switch to Decrypt tab]**

"Now let's decrypt it. I'll paste the encrypted text, select Caesar Cipher again, and click Decrypt."

**[Show decryption working]**

"Perfect! We get back our original message 'Hello World'."

---

### Demonstration 2: AES-256 Encryption (1 minute)

**[Switch to Encrypt tab]**

"Now let's try something more advanced - AES-256, which is used by governments for classified information."

**[Type plaintext]**
- Input: `This is confidential data!`

**[Select AES from dropdown and encrypt]**

"Notice that the encrypted output is much longer and appears random. This is because AES-256 uses a 256-bit key and includes an initialization vector for security."

**[Show the encrypted text]**

"The format is IV::Ciphertext, both base64 encoded."

**[Decrypt the message]**

"And decrypting it with the same algorithm gives us back the original message perfectly."

---

### Demonstration 3: RSA Public-Key Encryption (1 minute)

**[Encrypt tab]**

"RSA is an asymmetric algorithm, meaning it uses different keys for encryption and decryption."

**[Type text]**
- Input: `Secure message using public-key cryptography`

**[Select RSA and encrypt]**

"RSA is particularly useful for secure key exchange and digital signatures. Notice the encrypted output is quite long because we're using 2048-bit keys."

**[Show decryption]**

"And decryption works seamlessly."

---

### Demonstration 4: SHA-256 Hashing (45 seconds)

**[Encrypt tab]**

"SHA-256 is different - it's a one-way hash function, meaning you cannot decrypt it."

**[Type text]**
- Input: `password123`

**[Select SHA-256 and hash]**

"This produces a fixed 256-bit hash represented as 64 hexadecimal characters. This is commonly used for password storage and data integrity verification."

**[Try to decrypt - show error]**

"If we try to decrypt a hash, the system correctly tells us that SHA-256 is one-way and cannot be decrypted."

---

### Demonstration 5: Base64 Encoding (30 seconds)

**[Show Base64]**

"Base64 is an encoding scheme, not encryption. It's used for transmitting binary data in text format."

**[Encode and decode]**
- Input: `Hello, Base64!`
- Output: `SGVsbG8sIEJhc2U2NCE=`

"As you can see, it's easily reversible."

---

### Demonstration 6: DES Encryption (30 seconds)

"DES is a legacy algorithm included for educational purposes. It's no longer considered secure due to its small key size."

**[Quick encrypt/decrypt demo]**

---

### Features Showcase (1 minute)

"Let me highlight the key features:"

**1. Input Validation**
**[Try to encrypt without text]**
"If I try to encrypt without entering text, I get a clear error message."

**[Try without selecting algorithm]**
"Same if I forget to select an algorithm."

**2. Copy to Clipboard**
**[Demonstrate copy button]**
"The copy button provides instant feedback when clicked."

**3. Responsive Design**
**[Resize browser window if possible]**
"The interface is fully responsive and works on any device."

**4. Algorithm Information**
**[Scroll to info section]**
"Each algorithm has detailed information and categorization by type."

---

### Technical Overview (45 seconds)

"From a technical perspective, this application uses:

**Backend:**
- Python Flask framework
- PyCryptodome library for encryption
- RESTful API architecture

**Frontend:**
- HTML5, CSS3 with modern gradients and animations
- Vanilla JavaScript with async/await
- Fetch API for backend communication

**Security Features:**
- Input validation
- Error handling
- Proper padding schemes
- Secure random number generation"

---

### Bonus Features (30 seconds)

"This project includes all bonus requirements:
✓ Full decryption support for all reversible algorithms
✓ SHA-256 hashing
✓ One-click copy to clipboard
✓ Modern, responsive UI
✓ Comprehensive error handling"

---

### Conclusion (30 seconds)

"This Web-Based Text Encryption Tool demonstrates:
- Multiple encryption algorithms (symmetric and asymmetric)
- Cryptographic hashing
- Modern web development practices
- Security best practices
- Educational value

The complete source code, documentation, and technical report are available in the project repository.

Thank you for watching!"

---

## Demo Checklist

Before recording:
- [ ] Server is running (python app.py)
- [ ] Browser is open to localhost:5000
- [ ] Clear all previous inputs
- [ ] Test all features work correctly
- [ ] Prepare example texts
- [ ] Check copy functionality
- [ ] Verify error messages display correctly

Recording tips:
- [ ] Use screen recording software (OBS, Loom, etc.)
- [ ] Record at 1080p minimum
- [ ] Speak clearly and at moderate pace
- [ ] Zoom in on important UI elements
- [ ] Show both successful and error cases
- [ ] Keep video 5-8 minutes total
- [ ] Add intro/outro screens if possible

---

## Example Test Inputs

**Caesar Cipher:**
- "Hello World"
- "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

**AES/DES:**
- "This is confidential data!"
- "Secure communication test"

**RSA:**
- "Public-key cryptography demonstration"

**Base64:**
- "Hello, Base64!"
- "test@email.com"

**SHA-256:**
- "password123"
- "SecureP@ssw0rd"


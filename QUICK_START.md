# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
cd Web-Based-Text-Encryption-Tool
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

---

## ✅ Verify Installation

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

## 🎯 Quick Test

1. **Encrypt Text:**
   - Enter: `Hello World`
   - Select: `Caesar Cipher`
   - Click: `Encrypt Text`
   - Result: `Khoor Zruog`

2. **Decrypt Text:**
   - Switch to Decrypt tab
   - Enter: `Khoor Zruog`
   - Select: `Caesar Cipher`
   - Click: `Decrypt Text`
   - Result: `Hello World`

---

## 🔧 Troubleshooting

### Issue: Module not found
```bash
pip install Flask flask-cors pycryptodome
```

### Issue: Port 5000 already in use
Edit `app.py` line 174:
```python
app.run(debug=True, port=5001)  # Change port number
```

### Issue: Template not found
Ensure folder structure:
```
Web-Based-Text-Encryption-Tool/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

---

## 📱 Browser Compatibility

Tested on:
- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari

---

## 🎓 For Submission

Include these files:
1. ✅ All source code
2. ✅ README.md (technical documentation)
3. ✅ REPORT.md (encryption techniques explanation)
4. ✅ requirements.txt (dependencies)
5. ✅ Demo video (record using DEMO_SCRIPT.md)
6. ✅ GitHub repository link

---

## 💡 Tips

- Press **Ctrl+Enter** to encrypt/decrypt quickly
- Use the **📋 button** to copy results
- Try all 6 algorithms to see different outputs
- SHA-256 cannot be decrypted (it's a hash)

---

## 🆘 Need Help?

1. Check README.md for detailed documentation
2. Review REPORT.md for encryption explanations
3. Ensure Python 3.8+ is installed
4. Verify all dependencies are installed

---

**Enjoy experimenting with cryptography! 🔐**


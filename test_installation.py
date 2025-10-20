#!/usr/bin/env python3
"""
Quick installation test script
Run this to verify all dependencies are installed correctly
"""

import sys

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing Python dependencies...\n")
    
    tests = [
        ("Flask", "flask"),
        ("Flask-CORS", "flask_cors"),
        ("PyCryptodome - AES", "Crypto.Cipher.AES"),
        ("PyCryptodome - DES", "Crypto.Cipher.DES"),
        ("PyCryptodome - RSA", "Crypto.PublicKey.RSA"),
        ("PyCryptodome - PKCS1_OAEP", "Crypto.Cipher.PKCS1_OAEP"),
        ("PyCryptodome - Padding", "Crypto.Util.Padding"),
        ("PyCryptodome - Random", "Crypto.Random"),
        ("hashlib (built-in)", "hashlib"),
        ("base64 (built-in)", "base64"),
    ]
    
    failed = []
    passed = 0
    
    for name, module in tests:
        try:
            __import__(module)
            print(f"✅ {name:<30} OK")
            passed += 1
        except ImportError as e:
            print(f"❌ {name:<30} FAILED")
            failed.append((name, module, str(e)))
    
    print(f"\n{'='*50}")
    print(f"Results: {passed}/{len(tests)} tests passed")
    print(f"{'='*50}\n")
    
    if failed:
        print("❌ Installation incomplete! Missing dependencies:\n")
        for name, module, error in failed:
            print(f"  • {name}")
        print("\nRun: pip install -r requirements.txt")
        return False
    else:
        print("✅ All dependencies installed correctly!")
        print("\nYou can now run the application:")
        print("  python app.py")
        return True

def test_file_structure():
    """Test if all required files exist"""
    print("\nChecking file structure...\n")
    
    import os
    
    required_files = [
        "app.py",
        "requirements.txt",
        "README.md",
        "REPORT.md",
        "templates/index.html",
        "static/style.css",
        "static/script.js",
    ]
    
    missing = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing.append(file)
    
    if missing:
        print(f"\n❌ Missing files: {', '.join(missing)}")
        return False
    else:
        print("\n✅ All required files present!")
        return True

def test_encryption_functions():
    """Quick test of encryption functions"""
    print("\nTesting encryption functions...\n")
    
    try:
        # Import encryption functions
        from app import (
            caesar_cipher_encrypt, caesar_cipher_decrypt,
            base64_encode, base64_decode,
            sha256_hash
        )
        
        # Test Caesar Cipher
        test_text = "Hello"
        encrypted = caesar_cipher_encrypt(test_text)
        decrypted = caesar_cipher_decrypt(encrypted)
        assert decrypted == test_text, "Caesar cipher failed"
        print(f"✅ Caesar Cipher: '{test_text}' → '{encrypted}' → '{decrypted}'")
        
        # Test Base64
        encoded = base64_encode(test_text)
        decoded = base64_decode(encoded)
        assert decoded == test_text, "Base64 failed"
        print(f"✅ Base64: '{test_text}' → '{encoded}' → '{decoded}'")
        
        # Test SHA-256
        hash_result = sha256_hash(test_text)
        assert len(hash_result) == 64, "SHA-256 failed"
        print(f"✅ SHA-256: '{test_text}' → '{hash_result[:32]}...'")
        
        print("\n✅ All encryption functions working!")
        return True
        
    except Exception as e:
        print(f"\n❌ Encryption test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("="*50)
    print("Web-Based Text Encryption Tool")
    print("Installation Verification Script")
    print("="*50)
    print()
    
    results = []
    
    # Test 1: Dependencies
    results.append(("Dependencies", test_imports()))
    
    # Test 2: File Structure
    results.append(("File Structure", test_file_structure()))
    
    # Test 3: Encryption Functions
    results.append(("Encryption Functions", test_encryption_functions()))
    
    # Summary
    print("\n" + "="*50)
    print("FINAL RESULTS")
    print("="*50)
    
    all_passed = True
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {name}")
        if not passed:
            all_passed = False
    
    print("="*50)
    
    if all_passed:
        print("\n🎉 Success! Your installation is complete and working!")
        print("\nNext steps:")
        print("1. Run: python app.py")
        print("2. Open browser to: http://localhost:5000")
        print("3. Test the application")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())


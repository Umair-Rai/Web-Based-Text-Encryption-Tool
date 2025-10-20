// Switch between Encrypt and Decrypt tabs
function switchTab(tabName) {
    // Hide all tab contents
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    
    // Remove active class from all tab buttons
    document.querySelectorAll('.tab-button').forEach(button => {
        button.classList.remove('active');
    });
    
    // Show selected tab content
    if (tabName === 'encrypt') {
        document.getElementById('encryptTab').classList.add('active');
        document.querySelector('.tab-button:first-child').classList.add('active');
    } else {
        document.getElementById('decryptTab').classList.add('active');
        document.querySelector('.tab-button:last-child').classList.add('active');
    }
    
    // Clear any existing messages
    clearMessages();
}

// Encrypt text
async function encryptText() {
    const text = document.getElementById('plainText').value.trim();
    const algorithm = document.getElementById('encryptAlgorithm').value;
    const cipherTextArea = document.getElementById('cipherText');
    
    // Clear previous messages
    clearMessages('encrypt');
    
    // Validation
    if (!text) {
        showError('encrypt', 'Please enter text to encrypt');
        return;
    }
    
    if (!algorithm) {
        showError('encrypt', 'Please select an encryption algorithm');
        return;
    }
    
    try {
        const response = await fetch('/encrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                algorithm: algorithm
            })
        });
        
        const data = await response.json();
        
        if (response.ok && data.success) {
            cipherTextArea.value = data.result;
            showSuccess('encrypt', 'Text encrypted successfully!');
        } else {
            showError('encrypt', data.error || 'Encryption failed');
        }
    } catch (error) {
        showError('encrypt', 'Network error. Please ensure the server is running.');
        console.error('Error:', error);
    }
}

// Decrypt text
async function decryptText() {
    const text = document.getElementById('encryptedText').value.trim();
    const algorithm = document.getElementById('decryptAlgorithm').value;
    const decryptedTextArea = document.getElementById('decryptedText');
    
    // Clear previous messages
    clearMessages('decrypt');
    
    // Validation
    if (!text) {
        showError('decrypt', 'Please enter text to decrypt');
        return;
    }
    
    if (!algorithm) {
        showError('decrypt', 'Please select a decryption algorithm');
        return;
    }
    
    try {
        const response = await fetch('/decrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                algorithm: algorithm
            })
        });
        
        const data = await response.json();
        
        if (response.ok && data.success) {
            decryptedTextArea.value = data.result;
            showSuccess('decrypt', 'Text decrypted successfully!');
        } else {
            showError('decrypt', data.error || 'Decryption failed');
        }
    } catch (error) {
        showError('decrypt', 'Network error. Please ensure the server is running.');
        console.error('Error:', error);
    }
}

// Copy text to clipboard
function copyToClipboard(textareaId) {
    const textarea = document.getElementById(textareaId);
    const text = textarea.value;
    
    if (!text) {
        return;
    }
    
    navigator.clipboard.writeText(text).then(() => {
        // Show temporary success message
        const button = event.target;
        const originalText = button.textContent;
        button.textContent = '✓';
        button.style.background = '#10b981';
        
        setTimeout(() => {
            button.textContent = originalText;
            button.style.background = '#667eea';
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy text:', err);
        alert('Failed to copy to clipboard');
    });
}

// Show error message
function showError(tab, message) {
    const errorDiv = document.getElementById(`${tab}Error`);
    errorDiv.textContent = message;
    errorDiv.classList.add('show');
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        errorDiv.classList.remove('show');
    }, 5000);
}

// Show success message
function showSuccess(tab, message) {
    const successDiv = document.getElementById(`${tab}Success`);
    successDiv.textContent = message;
    successDiv.classList.add('show');
    
    // Auto-hide after 3 seconds
    setTimeout(() => {
        successDiv.classList.remove('show');
    }, 3000);
}

// Clear all messages
function clearMessages(tab = null) {
    if (tab) {
        document.getElementById(`${tab}Error`).classList.remove('show');
        document.getElementById(`${tab}Success`).classList.remove('show');
    } else {
        document.querySelectorAll('.error-message, .success-message').forEach(msg => {
            msg.classList.remove('show');
        });
    }
}

// Add keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + Enter to encrypt/decrypt
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        const activeTab = document.querySelector('.tab-content.active');
        if (activeTab.id === 'encryptTab') {
            encryptText();
        } else {
            decryptText();
        }
    }
});


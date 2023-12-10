def rotate_character(c, n):
    """Rotate a character by n positions."""
    if c.isalpha():
        start = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - start + n) % 26 + start)
    return c

def encrypt_rot26(text):
    """Encrypt text using ROT26."""
    return ''.join(rotate_character(c, 26) for c in text)

def decrypt_rot26(text):
    """Decrypt text using ROT26."""
    return ''.join(rotate_character(c, 26) for c in text)

# Example usage
original_text = input("What do you want to encrypt / Decrypt : )
encrypted_text = encrypt_rot26(original_text)
decrypted_text = decrypt_rot26(encrypted_text)

print("Original Text:", original_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

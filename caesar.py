def encrypt(key,plaintext):
    
    print(plaintext)
    print(key)
    ciphertext=""

    for char in plaintext:
        ciphertext += chr((ord(char) + key-65) % 26 + 65)
        
    print(ciphertext)

    return ciphertext

def decrypt(key,ciphertext):
    
    print(ciphertext)
    print(key)

    plaintext=""

    for char in ciphertext:
        plaintext += chr((ord(char) - key - 65) % 26 + 65)
        
    print(plaintext)

    return plaintext

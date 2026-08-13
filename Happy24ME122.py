# Caesar Cipher Encryption and Decryption

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted = encrypt(message, shift)
decrypted = encrypt(encrypted, -shift)

print("\nOriginal Message :", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
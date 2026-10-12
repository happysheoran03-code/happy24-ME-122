
def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix_chars = []

    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char.isalpha() and char not in matrix_chars:
            matrix_chars.append(char)

    return [matrix_chars[i:i+5] for i in range(0, 25, 5)]


def prepare_text(text):
    text = ''.join(c for c in text.upper() if c.isalpha())
    text = text.replace("J", "I")
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            b = 'X'
            i += 1
        elif text[i] == text[i + 1]:
            b = 'X'
            i += 1
        else:
            b = text[i + 1]
            i += 2

        pairs.append(a + b)

    return pairs


def playfair(text, matrix, encrypt=True):
    result = ""
    shift = 1 if encrypt else -1

    for pair in prepare_text(text):
        a, b = pair
        r1, c1 = next((r, c) for r in range(5)
                      for c in range(5) if matrix[r][c] == a)
        r2, c2 = next((r, c) for r in range(5)
                      for c in range(5) if matrix[r][c] == b)

        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5]
            result += matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1]
            result += matrix[(r2 + shift) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")

matrix = generate_key_matrix(key)

print("\nKey Matrix:")
for row in matrix:
    print(" ".join(row))

ciphertext = playfair(plaintext, matrix, True)
print("\nEncrypted Text:", ciphertext)

decrypted_text = playfair(ciphertext, matrix, False)
print("Decrypted Text:", decrypted_text)

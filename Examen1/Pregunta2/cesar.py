def caesar_cipher(message, shift):
    return ''.join(
        chr((ord(char) - base + shift) % 26 + base)
        if char.isalpha() else char
        for char in message
        for base in [ord('A') if char.isupper() else ord('a')]
    )


name = "Enrique Ulises Baez Gomez Tagle"
shift_value = 3
encrypted_name = caesar_cipher(name, shift_value)
print(f"Ciphered name: {encrypted_name}")

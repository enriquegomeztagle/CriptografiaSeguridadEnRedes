def substitution_cipher(name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    
    return ''.join(
        reversed_alphabet[alphabet.index(char)] if char.isalpha() else char
        for char in name.lower()
    )


name = "Enrique Ulises Baez Gomez Tagle"
encrypted_name = substitution_cipher(name)
print(f"Ciphered name: {encrypted_name}")

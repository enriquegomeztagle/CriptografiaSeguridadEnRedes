def substitution_cipher(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    
    return ''.join(
        reversed_alphabet[alphabet.index(char)] if char.isalpha() else char
        for char in message.lower()
    )


original_message = "Enrique Ulises Baez Gomez Tagle"
encrypted_name = substitution_cipher(original_message)
print(f"Ciphered name: {encrypted_name}")

def vigenere_cipher(name, key):
    result = []
    key_repeated = (key * (len(name) // len(key)) + key[:len(name) % len(key)])
    
    key_index = 0
    for char in name:
        if char.isalpha():
            base_char = ord('A') if char.isupper() else ord('a')
            shift = (ord(char) - base_char + ord(key_repeated[key_index].upper()) - ord('A')) % 26
            result.append(chr(base_char + shift))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)


name = "Enrique Ulises Baez Gomez Tagle"
key = "SHPONIC"
encrypted_name = vigenere_cipher(name, key)
print(f"Ciphered name: {encrypted_name}")

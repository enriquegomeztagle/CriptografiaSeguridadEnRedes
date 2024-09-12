import numpy as np

def hill_cipher(name, key_matrix):
    name = name.upper()
    matrix_size = len(key_matrix)
    name_numeric = [ord(char) - ord('A') for char in name if char.isalpha()]
    
    while len(name_numeric) % matrix_size != 0:
        name_numeric.append(23)
    
    key_matrix = np.array(key_matrix)
    
    cipher_name = []
    for i in range(0, len(name_numeric), matrix_size):
        block = np.array(name_numeric[i:i + matrix_size])
        encrypted_block = np.dot(key_matrix, block) % 26
        cipher_name.extend(chr(num + ord('A')) for num in encrypted_block)
    
    return ''.join(cipher_name)

name = "Enrique Ulises Baez Gomez Tagle"
key_matrix = [
    [2, 4, 12],
    [9, 1, 6],
    [7, 5, 3]
]
encrypted_name = hill_cipher(name, key_matrix)
print(f"Ciphered name: {encrypted_name}")

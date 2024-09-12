import string

def generate_playfair_matrix(key):
    alphabet = string.ascii_uppercase.replace('J', '')
    matrix = []
    seen = set()

    for letter in key.upper():
        if letter in alphabet and letter not in seen:
            matrix.append(letter)
            seen.add(letter)
    
    matrix.extend([letter for letter in alphabet if letter not in seen])
    
    return [matrix[i:i+5] for i in range(0, len(matrix), 5)]

def playfair_cipher(text, key):
    matrix = generate_playfair_matrix(key)
    processed_text = ''.join([char.upper().replace('J', 'I') for char in text if char.isalpha()])
    
    if len(processed_text) % 2 != 0:
        processed_text += 'X'

    def find_position(letter):
        for row, row_content in enumerate(matrix):
            if letter in row_content:
                return row, row_content.index(letter)
        return None

    result = []
    for i in range(0, len(processed_text), 2):
        letter1, letter2 = processed_text[i], processed_text[i+1]
        
        position1 = find_position(letter1)
        position2 = find_position(letter2)

        if position1 is None or position2 is None:
            raise ValueError(f"Letter '{letter1}' or '{letter2}' not found in matrix.")

        row1, col1 = position1
        row2, col2 = position2

        if row1 == row2:
            result.append(matrix[row1][(col1+1) % 5])
            result.append(matrix[row2][(col2+1) % 5])
        
        elif col1 == col2:
            result.append(matrix[(row1+1) % 5][col1])
            result.append(matrix[(row2+1) % 5][col2])
        
        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])

    return ''.join(result)


name = "Enrique Ulises Baez Gomez Tagle"
key = "SHPONIC"
encrypted_name = playfair_cipher(name, key)
print(f"Ciphered name: {encrypted_name}")

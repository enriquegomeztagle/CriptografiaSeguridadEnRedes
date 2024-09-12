def vigenere_cipher(text, key):
    result = []
    key_repeated = (key * (len(text) // len(key)) + key[:len(text) % len(key)])
    
    key_index = 0
    for char in text:
        if char.isalpha():
            base_char = ord('A') if char.isupper() else ord('a')
            shift = (ord(char) - base_char + ord(key_repeated[key_index].upper()) - ord('A')) % 26
            result.append(chr(base_char + shift))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)


text = """
fi f sorcdkh tlqk jb rqtrowelbvq
kxqa
welp klov veufqb, weh dhkwih
plk lp welp:
pv ofsp, wtr yorvelkj mlijoljv,
ohxgv vqdkg
qr pplrqk qkxw orrje wlxzk tlqk x
wbqaho nfvp.
"""

key = "dx"
encrypted_text = vigenere_cipher(text, key)
print(f"Ciphered text: {encrypted_text}")

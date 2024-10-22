import numpy as np

# S-box completa para SubBytes
s_box = [
    [
        0x63,
        0x7C,
        0x77,
        0x7B,
        0xF2,
        0x6B,
        0x6F,
        0xC5,
        0x30,
        0x01,
        0x67,
        0x2B,
        0xFE,
        0xD7,
        0xAB,
        0x76,
    ],
    [
        0xCA,
        0x82,
        0xC9,
        0x7D,
        0xFA,
        0x59,
        0x47,
        0xF0,
        0xAD,
        0xD4,
        0xA2,
        0xAF,
        0x9C,
        0xA4,
        0x72,
        0xC0,
    ],
    [
        0xB7,
        0xFD,
        0x93,
        0x26,
        0x36,
        0x3F,
        0xF7,
        0xCC,
        0x34,
        0xA5,
        0xE5,
        0xF1,
        0x71,
        0xD8,
        0x31,
        0x15,
    ],
    [
        0x04,
        0xC7,
        0x23,
        0xC3,
        0x18,
        0x96,
        0x05,
        0x9A,
        0x07,
        0x12,
        0x80,
        0xE2,
        0xEB,
        0x27,
        0xB2,
        0x75,
    ],
    [
        0x09,
        0x83,
        0x2C,
        0x1A,
        0x1B,
        0x6E,
        0x5A,
        0xA0,
        0x52,
        0x3B,
        0xD6,
        0xB3,
        0x29,
        0xE3,
        0x2F,
        0x84,
    ],
    [
        0x53,
        0xD1,
        0x00,
        0xED,
        0x20,
        0xFC,
        0xB1,
        0x5B,
        0x6A,
        0xCB,
        0xBE,
        0x39,
        0x4A,
        0x4C,
        0x58,
        0xCF,
    ],
    [
        0xD0,
        0xEF,
        0xAA,
        0xFB,
        0x43,
        0x4D,
        0x33,
        0x85,
        0x45,
        0xF9,
        0x02,
        0x7F,
        0x50,
        0x3C,
        0x9F,
        0xA8,
    ],
    [
        0x51,
        0xA3,
        0x40,
        0x8F,
        0x92,
        0x9D,
        0x38,
        0xF5,
        0xBC,
        0xB6,
        0xDA,
        0x21,
        0x10,
        0xFF,
        0xF3,
        0xD2,
    ],
    [
        0xCD,
        0x0C,
        0x13,
        0xEC,
        0x5F,
        0x97,
        0x44,
        0x17,
        0xC4,
        0xA7,
        0x7E,
        0x3D,
        0x64,
        0x5D,
        0x19,
        0x73,
    ],
    [
        0x60,
        0x81,
        0x4F,
        0xDC,
        0x22,
        0x2A,
        0x90,
        0x88,
        0x46,
        0xEE,
        0xB8,
        0x14,
        0xDE,
        0x5E,
        0x0B,
        0xDB,
    ],
    [
        0xE0,
        0x32,
        0x3A,
        0x0A,
        0x49,
        0x06,
        0x24,
        0x5C,
        0xC2,
        0xD3,
        0xAC,
        0x62,
        0x91,
        0x95,
        0xE4,
        0x79,
    ],
    [
        0xE7,
        0xC8,
        0x37,
        0x6D,
        0x8D,
        0xD5,
        0x4E,
        0xA9,
        0x6C,
        0x56,
        0xF4,
        0xEA,
        0x65,
        0x7A,
        0xAE,
        0x08,
    ],
    [
        0xBA,
        0x78,
        0x25,
        0x2E,
        0x1C,
        0xA6,
        0xB4,
        0xC6,
        0xE8,
        0xDD,
        0x74,
        0x1F,
        0x4B,
        0xBD,
        0x8B,
        0x8A,
    ],
    [
        0x70,
        0x3E,
        0xB5,
        0x66,
        0x48,
        0x03,
        0xF6,
        0x0E,
        0x61,
        0x35,
        0x57,
        0xB9,
        0x86,
        0xC1,
        0x1D,
        0x9E,
    ],
    [
        0xE1,
        0xF8,
        0x98,
        0x11,
        0x69,
        0xD9,
        0x8E,
        0x94,
        0x9B,
        0x1E,
        0x87,
        0xE9,
        0xCE,
        0x55,
        0x28,
        0xDF,
    ],
    [
        0x8C,
        0xA1,
        0x89,
        0x0D,
        0xBF,
        0xE6,
        0x42,
        0x68,
        0x41,
        0x99,
        0x2D,
        0x0F,
        0xB0,
        0x54,
        0xBB,
        0x16,
    ],
]

# Matriz para MixColumns
mix_columns_matrix = np.array(
    [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]], dtype=np.uint8
)

# Rcon para la expansión de la llave
rcon = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1B, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00],
]


# Función SubBytes
def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            row = state[i][j] >> 4
            col = state[i][j] & 0x0F
            state[i][j] = s_box[row][col]
    return state


# Función ShiftRows
def shift_rows(state):
    state[1] = np.roll(state[1], -1)
    state[2] = np.roll(state[2], -2)
    state[3] = np.roll(state[3], -3)
    return state


# Función para multiplicación en el campo de Galois
def galois_multiplication(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        carry = a & 0x80
        a <<= 1
        if carry:
            a ^= 0x1B
        b >>= 1
    return p


# Función MixColumns
def mix_columns(state):
    result = np.zeros((4, 4), dtype=np.uint8)
    for i in range(4):
        for j in range(4):
            result[i][j] = (
                galois_multiplication(mix_columns_matrix[i][0], state[0][j])
                ^ galois_multiplication(mix_columns_matrix[i][1], state[1][j])
                ^ galois_multiplication(mix_columns_matrix[i][2], state[2][j])
                ^ galois_multiplication(mix_columns_matrix[i][3], state[3][j])
            )
    return result


# Función AddRoundKey
def add_round_key(state, round_key):
    return np.bitwise_xor(state, round_key)


# Expansión de llaves
def key_expansion(key):
    expanded_key = np.zeros((44, 4), dtype=np.uint8)
    expanded_key[0:4] = np.array(key).reshape(4, 4)
    for i in range(4, 44):
        temp = expanded_key[i - 1]
        if i % 4 == 0:
            temp = np.roll(temp, -1)
            temp = [s_box[b >> 4][b & 0x0F] for b in temp]
            temp = np.bitwise_xor(temp, rcon[(i // 4) - 1])
        expanded_key[i] = np.bitwise_xor(expanded_key[i - 4], temp)
    return expanded_key


# Función principal AES-128
def aes_encrypt(plaintext, key):
    state = np.array(plaintext).reshape(4, 4)
    round_keys = key_expansion(key)

    state = add_round_key(state, round_keys[0:4])

    for round in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[round * 4 : (round + 1) * 4])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[40:44])

    return state.flatten().tolist()


# Convertir el ciphertext a hexadecimal
def bytes_to_hex(ciphertext):
    return "".join(format(byte, "02x") for byte in ciphertext)


# Función para convertir texto a bytes y rellenar si es necesario
def text_to_bytes(text):
    text_bytes = [ord(char) for char in text]
    while len(text_bytes) < 16:
        text_bytes.append(0x00)  # Rellenar con ceros si es necesario
    return text_bytes[:16]  # Asegurarse de que tenga exactamente 16 bytes


# Función para ingresar la llave
def key_to_bytes(key_input):
    key_bytes = [ord(char) for char in key_input]
    while len(key_bytes) < 16:
        key_bytes.append(0x00)  # Rellenar con ceros si es necesario
    return key_bytes[:16]  # Asegurarse de que tenga exactamente 16 bytes


# Flujo principal del programa
def main():
    # Están hardcodeadas la llave y el texto a cifrar
    key_input = "thisismadeoflove"
    plaintext_input = "Odi et amo. Quare id faciam, fortasse requiris. Nescio, sed fieri sentio et excrucior."

    key = key_to_bytes(key_input)
    plaintext_bytes = [
        text_to_bytes(plaintext_input[i : i + 16])
        for i in range(0, len(plaintext_input), 16)
    ]

    ciphertext = []
    for block in plaintext_bytes:
        encrypted_block = aes_encrypt(block, key)
        ciphertext.extend(encrypted_block)

    ciphertext_hex = "".join("{:02x}".format(b) for b in ciphertext)
    print("Texto cifrado (Ciphertext en hexadecimal):", ciphertext_hex)


if __name__ == "__main__":
    main()

"""
Texto cifrado (Ciphertext en hexadecimal): 4aae1fd1784c2a9d88ba8862b32d9510a948d411661dfc66c26131a78cad7540c85647dd43ad2155621cc801de2957fa0885b18a6ddcc8b7c63747e1340c78f274a37ebce5e35e3b8ee6df56452d6ae02ec1db544c1d413d767920db5d48896e
"""

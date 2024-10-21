import numpy as np

# Complete S-box for SubBytes
S_BOX = [
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

# Inverse S-box for InvSubBytes
INV_S_BOX = [
    [
        0x52,
        0x09,
        0x6A,
        0xD5,
        0x30,
        0x36,
        0xA5,
        0x38,
        0xBF,
        0x40,
        0xA3,
        0x9E,
        0x81,
        0xF3,
        0xD7,
        0xFB,
    ],
    [
        0x7C,
        0xE3,
        0x39,
        0x82,
        0x9B,
        0x2F,
        0xFF,
        0x87,
        0x34,
        0x8E,
        0x43,
        0x44,
        0xC4,
        0xDE,
        0xE9,
        0xCB,
    ],
    [
        0x54,
        0x7B,
        0x94,
        0x32,
        0xA6,
        0xC2,
        0x23,
        0x3D,
        0xEE,
        0x4C,
        0x95,
        0x0B,
        0x42,
        0xFA,
        0xC3,
        0x4E,
    ],
    [
        0x08,
        0x2E,
        0xA1,
        0x66,
        0x28,
        0xD9,
        0x24,
        0xB2,
        0x76,
        0x5B,
        0xA2,
        0x49,
        0x6D,
        0x8B,
        0xD1,
        0x25,
    ],
    [
        0x72,
        0xF8,
        0xF6,
        0x64,
        0x86,
        0x68,
        0x98,
        0x16,
        0xD4,
        0xA4,
        0x5C,
        0xCC,
        0x5D,
        0x65,
        0xB6,
        0x92,
    ],
    [
        0x6C,
        0x70,
        0x48,
        0x50,
        0xFD,
        0xED,
        0xB9,
        0xDA,
        0x5E,
        0x15,
        0x46,
        0x57,
        0xA7,
        0x8D,
        0x9D,
        0x84,
    ],
    [
        0x90,
        0xD8,
        0xAB,
        0x00,
        0x8C,
        0xBC,
        0xD3,
        0x0A,
        0xF7,
        0xE4,
        0x58,
        0x05,
        0xB8,
        0xB3,
        0x45,
        0x06,
    ],
    [
        0xD0,
        0x2C,
        0x1E,
        0x8F,
        0xCA,
        0x3F,
        0x0F,
        0x02,
        0xC1,
        0xAF,
        0xBD,
        0x03,
        0x01,
        0x13,
        0x8A,
        0x6B,
    ],
    [
        0x3A,
        0x91,
        0x11,
        0x41,
        0x4F,
        0x67,
        0xDC,
        0xEA,
        0x97,
        0xF2,
        0xCF,
        0xCE,
        0xF0,
        0xB4,
        0xE6,
        0x73,
    ],
    [
        0x96,
        0xAC,
        0x74,
        0x22,
        0xE7,
        0xAD,
        0x35,
        0x85,
        0xE2,
        0xF9,
        0x37,
        0xE8,
        0x1C,
        0x75,
        0xDF,
        0x6E,
    ],
    [
        0x47,
        0xF1,
        0x1A,
        0x71,
        0x1D,
        0x29,
        0xC5,
        0x89,
        0x6F,
        0xB7,
        0x62,
        0x0E,
        0xAA,
        0x18,
        0xBE,
        0x1B,
    ],
    [
        0xFC,
        0x56,
        0x3E,
        0x4B,
        0xC6,
        0xD2,
        0x79,
        0x20,
        0x9A,
        0xDB,
        0xC0,
        0xFE,
        0x78,
        0xCD,
        0x5A,
        0xF4,
    ],
    [
        0x1F,
        0xDD,
        0xA8,
        0x33,
        0x88,
        0x07,
        0xC7,
        0x31,
        0xB1,
        0x12,
        0x10,
        0x59,
        0x27,
        0x80,
        0xEC,
        0x5F,
    ],
    [
        0x60,
        0x51,
        0x7F,
        0xA9,
        0x19,
        0xB5,
        0x4A,
        0x0D,
        0x2D,
        0xE5,
        0x7A,
        0x9F,
        0x93,
        0xC9,
        0x9C,
        0xEF,
    ],
    [
        0xA0,
        0xE0,
        0x3B,
        0x4D,
        0xAE,
        0x2A,
        0xF5,
        0xB0,
        0xC8,
        0xEB,
        0xBB,
        0x3C,
        0x83,
        0x53,
        0x99,
        0x61,
    ],
    [
        0x17,
        0x2B,
        0x04,
        0x7E,
        0xBA,
        0x77,
        0xD6,
        0x26,
        0xE1,
        0x69,
        0x14,
        0x63,
        0x55,
        0x21,
        0x0C,
        0x7D,
    ],
]

# Rcon for key expansion
RCON = [
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


def inv_sub_bytes(state):
    """Perform the InvSubBytes step using the inverse S-box."""
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            row = byte >> 4
            col = byte & 0x0F
            state[i][j] = INV_S_BOX[row][col]
    return state


def inv_shift_rows(state):
    """Perform the InvShiftRows step by rotating the rows to the right."""
    state[1] = np.roll(state[1], 1)
    state[2] = np.roll(state[2], 2)
    state[3] = np.roll(state[3], 3)
    return state


def galois_multiplication(a, b):
    """Perform multiplication in the Galois Field GF(2^8)."""
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        high_bit_set = a & 0x80
        a = (a << 1) & 0xFF  # Ensure a stays within 8 bits
        if high_bit_set:
            a ^= 0x1B
        b >>= 1
    return p


def inv_mix_columns(state):
    """Perform the InvMixColumns step using the inverse mix columns matrix."""
    inv_matrix = np.array(
        [
            [0x0E, 0x0B, 0x0D, 0x09],
            [0x09, 0x0E, 0x0B, 0x0D],
            [0x0D, 0x09, 0x0E, 0x0B],
            [0x0B, 0x0D, 0x09, 0x0E],
        ],
        dtype=np.uint8,
    )
    result = np.zeros((4, 4), dtype=np.uint8)
    for col in range(4):
        for row in range(4):
            result[row][col] = (
                galois_multiplication(inv_matrix[row][0], state[0][col])
                ^ galois_multiplication(inv_matrix[row][1], state[1][col])
                ^ galois_multiplication(inv_matrix[row][2], state[2][col])
                ^ galois_multiplication(inv_matrix[row][3], state[3][col])
            )
    return result


def add_round_key(state, round_key):
    """Add (XOR) the round key to the state."""
    return np.bitwise_xor(state, round_key)


def key_expansion(key):
    """Expand the cipher key into an array of round keys."""
    expanded_key = np.zeros((44, 4), dtype=np.uint8)
    expanded_key[:4] = np.array(key).reshape(4, 4)
    for i in range(4, 44):
        temp = expanded_key[i - 1]
        if i % 4 == 0:
            temp = np.roll(temp, -1)
            temp = [S_BOX[b >> 4][b & 0x0F] for b in temp]
            temp = np.bitwise_xor(temp, RCON[(i // 4) - 1])
        expanded_key[i] = np.bitwise_xor(expanded_key[i - 4], temp)
    return expanded_key


def aes_decrypt(ciphertext, key):
    """Decrypt the ciphertext using AES-128 decryption algorithm."""
    state = np.array(ciphertext).reshape(4, 4)
    round_keys = key_expansion(key)

    # Initial AddRoundKey
    state = add_round_key(state, round_keys[40:44])

    # Perform 9 rounds
    for round_num in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[round_num * 4 : (round_num + 1) * 4])
        state = inv_mix_columns(state)

    # Final round (without InvMixColumns)
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[0:4])

    return state.flatten().tolist()


def key_to_bytes(key_input):
    """Convert the key string to a list of 16 bytes."""
    key_bytes = [ord(char) for char in key_input]
    key_bytes += [0x00] * (16 - len(key_bytes))  # Pad with zeros if necessary
    return key_bytes[:16]


def decrypt_main():
    """Main function to handle user input and perform decryption."""
    key_input = input("Introduce la clave de cifrado (16 caracteres): ")
    key = key_to_bytes(key_input)

    ciphertext_input = input(
        "Introduce el texto cifrado (hexadecimal, 32 caracteres): "
    )
    try:
        ciphertext = [
            int(ciphertext_input[i : i + 2], 16)
            for i in range(0, len(ciphertext_input), 2)
        ]
        if len(ciphertext) != 16:
            raise ValueError
    except ValueError:
        print(
            "Error: El texto cifrado debe ser un string hexadecimal de 32 caracteres."
        )
        return

    decrypted_text = aes_decrypt(ciphertext, key)
    decrypted_text_str = "".join(chr(b) for b in decrypted_text).rstrip("\x00")

    print("Texto descifrado:", decrypted_text_str)


if __name__ == "__main__":
    decrypt_main()

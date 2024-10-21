"""
This module provides an AES-128 encryption and decryption tool with a command-line interface.

The user can choose between encrypting or decrypting a message using AES-128. The key and plaintext
are limited to 16 characters. 

Dependencies:
- numpy
- colorama
"""

import numpy as np
from colorama import Fore, Style


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


def galois_multiplication(a, b):
    """
    Performs Galois multiplication on two numbers using the AES polynomial (0x1B).
    """
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        high_bit_set = a & 0x80
        a = (a << 1) & 0xFF
        if high_bit_set:
            a ^= 0x1B
        b >>= 1
    return p


def sub_bytes(state):
    """
    Substitute each byte in the state matrix with a byte from the S-Box according 
    to the byte's row and column values.

    Args:
        state (list): The 4x4 state matrix to perform byte substitution on.

    Returns:
        list: The state matrix after byte substitution.
    """
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            row = byte >> 4
            col = byte & 0x0F
            state[i][j] = S_BOX[row][col]
    return state


def shift_rows(state):
    """
    Shifts the rows of the AES state matrix cyclically to the left.

    Args:
        state (list): The AES state matrix.

    Returns:
        list: The state matrix with rows shifted.
    """
    state[1] = np.roll(state[1], -1)
    state[2] = np.roll(state[2], -2)
    state[3] = np.roll(state[3], -3)
    return state


def mix_columns(state):
    """
    Perform the MixColumns operation on the AES state using the given mix_matrix.

    Args:
        state (np.array): The current state of the AES encryption.

    Returns:
        np.array: The state after applying the MixColumns operation.
    """
    mix_matrix = np.array(
        [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]], dtype=np.uint8
    )
    result = np.zeros((4, 4), dtype=np.uint8)
    for col in range(4):
        for row in range(4):
            result[row][col] = (
                galois_multiplication(mix_matrix[row][0], state[0][col])
                ^ galois_multiplication(mix_matrix[row][1], state[1][col])
                ^ galois_multiplication(mix_matrix[row][2], state[2][col])
                ^ galois_multiplication(mix_matrix[row][3], state[3][col])
            )
    return result


def add_round_key(state, round_key):
    """
    Performs an XOR operation between the state and the round key.

    Parameters:
    - state: numpy array representing the current state of the encryption
    - round_key: numpy array representing the round key to be added

    Returns:
    - numpy array resulting from the XOR operation
    """
    return np.bitwise_xor(state, round_key)


def inv_sub_bytes(state):
    """
    Perform inverse SubBytes operation on the given state using the INV_S_BOX lookup table.

    Args:
        state (list): The 4x4 matrix representing the current state.

    Returns:
        list: The state matrix after applying the inverse SubBytes operation.
    """
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            row = byte >> 4
            col = byte & 0x0F
            state[i][j] = INV_S_BOX[row][col]
    return state


def inv_shift_rows(state):
    """
    Performs inverse ShiftRows operation on the AES state matrix.

    Shifts the rows of the state matrix to the right by varying offsets for each row.
    The first row remains unchanged, the second row is shifted right by 1 position,
    the third row by 2 positions, and the fourth row by 3 positions.

    Parameters:
    state (list): The AES state matrix to apply the inverse ShiftRows operation on.

    Returns:
    list: The state matrix after applying the inverse ShiftRows operation.
    """
    state[1] = np.roll(state[1], 1)
    state[2] = np.roll(state[2], 2)
    state[3] = np.roll(state[3], 3)
    return state


def inv_mix_columns(state):
    """
    Perform inverse MixColumns operation on the AES state matrix using the given inverse matrix.

    Args:
        state (np.array): The 4x4 AES state matrix to apply the operation on.

    Returns:
        np.array: The resulting state matrix after the inverse MixColumns operation.
    """
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


def key_expansion(key):
    """
    Expand the given AES-128 key to generate a 44x4 expanded key matrix.

    Parameters:
    key (list): The original 16-byte key to be expanded.

    Returns:
    numpy.ndarray: The expanded key matrix for AES encryption.
    """
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


def aes_encrypt(plaintext, key):
    """
    Encrypts the given plaintext using AES-128 encryption algorithm with the provided key.

    Parameters:
    - plaintext (list): The plaintext to be encrypted.
    - key (list): The 16-byte key used for encryption.

    Returns:
    - list: The encrypted ciphertext as a flattened list.
    """
    state = np.array(plaintext).reshape(4, 4)
    round_keys = key_expansion(key)
    state = add_round_key(state, round_keys[0:4])
    for round_num in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[round_num * 4 : (round_num + 1) * 4])
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[40:44])
    return state.flatten().tolist()


def aes_decrypt(ciphertext, key):
    """
    Decrypts the given AES-128 ciphertext using the provided key.

    Parameters:
    - ciphertext (list): The encrypted data to be decrypted.
    - key (list): The 16-byte key used for decryption.

    Returns:
    - list: The decrypted data after applying AES decryption.
    """
    state = np.array(ciphertext).reshape(4, 4)
    round_keys = key_expansion(key)
    state = add_round_key(state, round_keys[40:44])
    for round_num in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[round_num * 4 : (round_num + 1) * 4])
        state = inv_mix_columns(state)
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[0:4])
    return state.flatten().tolist()


def key_to_bytes(key_input):
    """
    Converts a given key input into a list of bytes limited to 16 elements 
    by padding with zeros if necessary.

    Parameters:
    key_input (str): The input key to be converted into bytes.

    Returns:
    list: A list of bytes representing the key, limited to 16 elements.
    """
    key_bytes = [ord(char) for char in key_input]
    key_bytes += [0x00] * (16 - len(key_bytes))
    return key_bytes[:16]


def bytes_to_hex(ciphertext):
    """
    Converts a list of bytes to a hexadecimal string.

    Parameters:
    ciphertext (list): List of bytes to convert to hexadecimal.

    Returns:
    str: Hexadecimal representation of the input bytes.
    """

    return "".join(format(byte, "02x") for byte in ciphertext)


def text_to_bytes(text):
    """
    Converts a text string to a list of bytes.

    Args:
        text (str): The input text to be converted.

    Returns:
        list: A list of bytes representing the text, padded with zeros to a length of 16 bytes.
    """
    text_bytes = [ord(char) for char in text]
    while len(text_bytes) < 16:
        text_bytes.append(0x00)
    return text_bytes[:16]


def main():
    """
    Runs a loop for AES-128 encryption and decryption options.
    
    Prints menu options for encryption, decryption, and exiting the program.
    Handles user input for key, text, and ciphertext.
    Performs encryption and decryption operations based on user choices.
    """
    while True:
        print(Fore.BLUE + "\n--- AES-128 Encryption/Decryption ---" + Style.RESET_ALL)
        print(Fore.BLUE + "1. Encrypt" + Style.RESET_ALL)
        print(Fore.BLUE + "2. Decrypt" + Style.RESET_ALL)
        print(Fore.BLUE + "3. Exit" + Style.RESET_ALL)
        choice = input("Select an option (1-3): ")

        if choice == "1":
            key_input = input(
                Fore.RED + "Enter encryption key (16 characters): " + Style.RESET_ALL
            )
            key = key_to_bytes(key_input)
            plaintext_input = input(
                Fore.RED
                + "Enter text to encrypt (max 16 characters): "
                + Style.RESET_ALL
            )
            plaintext = text_to_bytes(plaintext_input)
            ciphertext = aes_encrypt(plaintext, key)
            ciphertext_hex = bytes_to_hex(ciphertext)
            print(
                Fore.RED + "Encrypted text (hexadecimal):" + Style.RESET_ALL,
                ciphertext_hex,
            )
        elif choice == "2":
            key_input = input(
                Fore.RED + "Enter encryption key (16 characters): " + Style.RESET_ALL
            )
            key = key_to_bytes(key_input)
            ciphertext_input = input(
                Fore.RED
                + "Enter encrypted text (hexadecimal, 32 characters): "
                + Style.RESET_ALL
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
                    Fore.RED
                    + "Error: Encrypted text must be a 32-character hexadecimal string."
                    + Style.RESET_ALL
                )
                continue
            decrypted_text = aes_decrypt(ciphertext, key)
            decrypted_text_str = "".join(chr(b) for b in decrypted_text).rstrip("\x00")
            print(Fore.RED + "Decrypted text:" + Style.RESET_ALL, decrypted_text_str)
        elif choice == "3":
            print(Fore.BLUE + "Exiting program." + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED + "Invalid option. Please select 1, 2, or 3." + Style.RESET_ALL
            )


if __name__ == "__main__":
    main()
